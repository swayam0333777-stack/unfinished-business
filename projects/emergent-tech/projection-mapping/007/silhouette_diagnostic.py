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

print("Diagnostic started.")
print("Press Q to quit.")

with PoseLandmarker.create_from_options(options) as landmarker:

    while True:

        success, frame = camera.read()

        if not success:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        results = landmarker.detect(mp_image)

        # Default black mask
        mask_display = np.zeros_like(frame)

        if results.segmentation_masks:

            mask = results.segmentation_masks[0].numpy_view()
            mask = np.squeeze(mask)

            mask = cv2.resize(
                mask,
                (frame.shape[1], frame.shape[0]),
                interpolation=cv2.INTER_LINEAR
            )

            # RAW segmentation directly from MediaPipe
            raw_mask = (mask * 255).astype(np.uint8)

            # Convert to 3-channel image
            mask_display = cv2.cvtColor(
                raw_mask,
                cv2.COLOR_GRAY2BGR
            )

        # Put camera and raw mask side by side
        camera_view = frame.copy()

        combined = np.hstack(
            (camera_view, mask_display)
        )

        cv2.imshow(
            "Camera | RAW MediaPipe Segmentation",
            combined
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()