import cv2
import mediapipe as mp
import numpy as np

BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

model_path = "pose_landmarker_full.task"

options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE,
    num_poses=1,
    output_segmentation_masks=True
)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Could not open webcam")
    exit()

previous_mask = None

print("Smooth silhouette started.")
print("Press Q to quit.")

with PoseLandmarker.create_from_options(options) as landmarker:

    while True:
        success, frame = camera.read()

        if not success:
            print("ERROR: Could not read webcam frame")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        results = landmarker.detect(mp_image)

        silhouette = np.zeros_like(frame)

        if results.segmentation_masks:

            mask = results.segmentation_masks[0].numpy_view()
            mask = np.squeeze(mask)

            mask = cv2.resize(
                mask,
                (frame.shape[1], frame.shape[0]),
                interpolation=cv2.INTER_LINEAR
            )

            if previous_mask is None:
                smooth_mask = mask
            else:
                smooth_mask = (
                    0.70 * previous_mask +
                    0.30 * mask
                )

            previous_mask = smooth_mask

            binary_mask = (smooth_mask > 0.5).astype(np.uint8) * 255

            kernel = np.ones((5, 5), np.uint8)

            binary_mask = cv2.morphologyEx(
                binary_mask,
                cv2.MORPH_CLOSE,
                kernel
            )

            binary_mask = cv2.GaussianBlur(
                binary_mask,
                (5, 5),
                0
            )

            _, binary_mask = cv2.threshold(
                binary_mask,
                127,
                255,
                cv2.THRESH_BINARY
            )

            silhouette[binary_mask > 0] = (255, 255, 255)

        cv2.imshow(
            "Smooth Human Silhouette",
            silhouette
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()