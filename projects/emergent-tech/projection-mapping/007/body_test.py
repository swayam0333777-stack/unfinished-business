import cv2
import mediapipe as mp

# Load MediaPipe Pose Landmarker
BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Location of our downloaded model
model_path = "pose_landmarker_lite.task"

# Configure the pose tracker
options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE,
    num_poses=1
)

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Could not open webcam")
    exit()

print("Body tracking started.")
print("Press Q to quit.")

with PoseLandmarker.create_from_options(options) as landmarker:

    while True:
        success, frame = camera.read()

        if not success:
            print("ERROR: Could not read webcam frame")
            break

        # Convert OpenCV BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert to MediaPipe image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        # Detect the body
        results = landmarker.detect(mp_image)

        # Draw the detected body landmarks
        if results.pose_landmarks:
            for landmarks in results.pose_landmarks:

                height, width, _ = frame.shape

                # Draw points
                for landmark in landmarks:
                    x = int(landmark.x * width)
                    y = int(landmark.y * height)

                    if 0 <= x < width and 0 <= y < height:
                        cv2.circle(
                            frame,
                            (x, y),
                            5,
                            (0, 255, 0),
                            -1
                        )

                # Draw connections between body landmarks
                connections = [
                    (0, 1), (1, 2), (2, 3), (3, 7),
                    (0, 4), (4, 5), (5, 6), (6, 8),
                    (9, 10),

                    (11, 12),

                    (11, 13), (13, 15),
                    (15, 17), (15, 19), (15, 21),

                    (12, 14), (14, 16),
                    (16, 18), (16, 20), (16, 22),

                    (11, 23),
                    (12, 24),
                    (23, 24),

                    (23, 25), (25, 27),
                    (27, 29), (27, 31),

                    (24, 26), (26, 28),
                    (28, 30), (28, 32)
                ]

                for start, end in connections:
                    x1 = int(landmarks[start].x * width)
                    y1 = int(landmarks[start].y * height)

                    x2 = int(landmarks[end].x * width)
                    y2 = int(landmarks[end].y * height)

                    if (
                        0 <= x1 < width and
                        0 <= y1 < height and
                        0 <= x2 < width and
                        0 <= y2 < height
                    ):
                        cv2.line(
                            frame,
                            (x1, y1),
                            (x2, y2),
                            (0, 255, 0),
                            2
                        )

        cv2.imshow("Full Body Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()