import cv2
import mediapipe as mp
import numpy as np
import time
import math
import pygame


# ============================================================
# MEDIAPIPE SETUP
# ============================================================

BaseOptions = mp.tasks.BaseOptions
VisionRunningMode = mp.tasks.vision.RunningMode

PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions

HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions


pose_options = PoseLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="pose_landmarker_full.task"
    ),
    running_mode=VisionRunningMode.VIDEO,
    num_poses=1,
    output_segmentation_masks=True
)


hand_options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="hand_landmarker.task"
    ),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=2
)


# ============================================================
# CAMERA
# ============================================================

camera = cv2.VideoCapture(0)

camera.set(
    cv2.CAP_PROP_FRAME_WIDTH,
    1280
)

camera.set(
    cv2.CAP_PROP_FRAME_HEIGHT,
    720
)

# Try to reduce camera buffering
camera.set(
    cv2.CAP_PROP_BUFFERSIZE,
    1
)


if not camera.isOpened():

    print("ERROR: Could not open camera.")
    exit()


# ============================================================
# FULLSCREEN WINDOW
# ============================================================

WINDOW_NAME = "Bond Silhouette"

cv2.namedWindow(
    WINDOW_NAME,
    cv2.WINDOW_NORMAL
)

cv2.setWindowProperty(
    WINDOW_NAME,
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)


print("Bond silhouette started.")
print("Press Q to quit.")


# ============================================================
# MUSIC
# ============================================================

music_enabled = False

try:

    pygame.mixer.init()

    pygame.mixer.music.load(
        "music.mp3"
    )

    pygame.mixer.music.set_volume(
        0.7
    )

    pygame.mixer.music.play()

    music_enabled = True

    print("Music started.")

except Exception as e:

    print("Music could not be started:")
    print(e)


# ============================================================
# SPIRAL SETTINGS
# ============================================================

NUM_BLADES = 12

ROTATION_SPEED = 0.7

START_RADIUS = 20

# Slow opening
OPENING_DURATION = 35.0

# Outer blade thickness
BLADE_WIDTH = 90

# Spiral curvature
SPIRAL_CURVE = 100


# ============================================================
# CREATE SPIRAL BLADE
# ============================================================

def create_blade(
    cx,
    cy,
    start_angle,
    rotation,
    inner_radius,
    outer_radius,
    width
):

    points = []

    point_count = 180


    # ========================================================
    # FIRST EDGE
    # ========================================================

    for i in range(
        point_count
    ):

        t = (
            i
            / (point_count - 1)
        )


        radius = (
            inner_radius
            + (
                outer_radius
                - inner_radius
            ) * t
        )


        angle = (
            start_angle
            + rotation
            + t
            * math.radians(
                SPIRAL_CURVE
            )
        )


        # Very thin near center
        # Thick toward outside

        local_width = (
            width
            * (t ** 1.8)
        )


        offset_angle = (
            angle
            + math.pi / 2
        )


        x = (
            cx
            + radius
            * math.cos(angle)
            + local_width
            * math.cos(
                offset_angle
            )
        )


        y = (
            cy
            + radius
            * math.sin(angle)
            + local_width
            * math.sin(
                offset_angle
            )
        )


        points.append(
            (
                int(x),
                int(y)
            )
        )


    # ========================================================
    # SECOND EDGE
    # ========================================================

    for i in range(
        point_count - 1,
        -1,
        -1
    ):

        t = (
            i
            / (point_count - 1)
        )


        radius = (
            inner_radius
            + (
                outer_radius
                - inner_radius
            ) * t
        )


        angle = (
            start_angle
            + rotation
            + t
            * math.radians(
                SPIRAL_CURVE
            )
        )


        local_width = (
            width
            * (t ** 1.8)
        )


        offset_angle = (
            angle
            - math.pi / 2
        )


        x = (
            cx
            + radius
            * math.cos(angle)
            + local_width
            * math.cos(
                offset_angle
            )
        )


        y = (
            cy
            + radius
            * math.sin(angle)
            + local_width
            * math.sin(
                offset_angle
            )
        )


        points.append(
            (
                int(x),
                int(y)
            )
        )


    return np.array(
        points,
        dtype=np.int32
    )


# ============================================================
# ANIMATION VARIABLES
# ============================================================

start_time = time.monotonic()

previous_body_mask = None

previous_center_x = None
previous_center_y = None


# ============================================================
# MEDIAPIPE
# ============================================================

with PoseLandmarker.create_from_options(
    pose_options
) as pose_landmarker, HandLandmarker.create_from_options(
    hand_options
) as hand_landmarker:


    while True:


        # ====================================================
        # READ CAMERA
        # ====================================================

        success, frame = camera.read()


        if not success:

            print(
                "Could not read camera."
            )

            break


        # ====================================================
        # MIRROR CAMERA
        # ====================================================

        frame = cv2.flip(
            frame,
            1
        )


        height, width, _ = (
            frame.shape
        )


        # ====================================================
        # MEDIAPIPE IMAGE
        # ====================================================

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )


        mp_image = mp.Image(
            image_format=
                mp.ImageFormat.SRGB,
            data=rgb
        )


        timestamp_ms = int(
            (
                time.monotonic()
                - start_time
            ) * 1000
        )


        # ====================================================
        # BODY TRACKING
        # ====================================================

        pose_result = (
            pose_landmarker
            .detect_for_video(
                mp_image,
                timestamp_ms
            )
        )


        body_mask = np.zeros(
            (
                height,
                width
            ),
            dtype=np.uint8
        )


        if pose_result.segmentation_masks:


            mask = (
                pose_result
                .segmentation_masks[0]
                .numpy_view()
            )


            mask = np.squeeze(
                mask
            )


            # =================================================
            # RESIZE SEGMENTATION MASK
            # =================================================

            mask = cv2.resize(
                mask,
                (
                    width,
                    height
                ),
                interpolation=
                    cv2.INTER_CUBIC
            )


            # =================================================
            # TEMPORAL SMOOTHING
            # =================================================

            if (
                previous_body_mask
                is None
            ):

                smooth_mask = mask

            else:

                smooth_mask = (
                    0.75
                    * previous_body_mask
                    + 0.25
                    * mask
                )


            previous_body_mask = (
                smooth_mask
            )


            # =================================================
            # SOFT MASK
            # =================================================

            body_mask = (
                smooth_mask * 255
            ).astype(
                np.uint8
            )


            # =================================================
            # SPATIAL SMOOTHING
            # =================================================

            body_mask = cv2.GaussianBlur(
                body_mask,
                (
                    9,
                    9
                ),
                0
            )


            # =================================================
            # CLEAN SMALL HOLES
            # =================================================

            kernel = np.ones(
                (
                    5,
                    5
                ),
                np.uint8
            )


            body_mask = (
                cv2.morphologyEx(
                    body_mask,
                    cv2.MORPH_CLOSE,
                    kernel
                )
            )


        # ====================================================
        # FIND PERSON CENTER
        # ====================================================

        person_center_x = (
            width // 2
        )

        person_center_y = (
            height // 2
        )


        if pose_result.pose_landmarks:


            landmarks = (
                pose_result
                .pose_landmarks[0]
            )


            # Shoulder + hip points

            important_points = [
                11,
                12,
                23,
                24
            ]


            valid_points = []


            for index in (
                important_points
            ):


                landmark = (
                    landmarks[index]
                )


                if (
                    landmark.visibility
                    > 0.5
                ):


                    x = int(
                        landmark.x
                        * width
                    )


                    y = int(
                        landmark.y
                        * height
                    )


                    x = max(
                        0,
                        min(
                            width - 1,
                            x
                        )
                    )


                    y = max(
                        0,
                        min(
                            height - 1,
                            y
                        )
                    )


                    valid_points.append(
                        (
                            x,
                            y
                        )
                    )


            if valid_points:


                person_center_x = int(
                    sum(
                        p[0]
                        for p in valid_points
                    )
                    / len(
                        valid_points
                    )
                )


                person_center_y = int(
                    sum(
                        p[1]
                        for p in valid_points
                    )
                    / len(
                        valid_points
                    )
                )


        # ====================================================
        # SMOOTH MOVING CENTER
        # ====================================================

        if (
            previous_center_x
            is None
        ):


            previous_center_x = (
                person_center_x
            )

            previous_center_y = (
                person_center_y
            )


        else:


            previous_center_x = int(
                0.88
                * previous_center_x
                + 0.12
                * person_center_x
            )


            previous_center_y = int(
                0.88
                * previous_center_y
                + 0.12
                * person_center_y
            )


        person_center_x = (
            previous_center_x
        )

        person_center_y = (
            previous_center_y
        )


        # ====================================================
        # HAND TRACKING
        # ====================================================

        hand_result = (
            hand_landmarker
            .detect_for_video(
                mp_image,
                timestamp_ms
            )
        )


        hand_mask = np.zeros(
            (
                height,
                width
            ),
            dtype=np.uint8
        )


        if hand_result.hand_landmarks:


            for hand in (
                hand_result.hand_landmarks
            ):


                points = []


                # =============================================
                # HAND LANDMARKS
                # =============================================

                for landmark in hand:


                    x = int(
                        landmark.x
                        * width
                    )


                    y = int(
                        landmark.y
                        * height
                    )


                    x = max(
                        0,
                        min(
                            width - 1,
                            x
                        )
                    )


                    y = max(
                        0,
                        min(
                            height - 1,
                            y
                        )
                    )


                    points.append(
                        (
                            x,
                            y
                        )
                    )


                if len(points) != 21:

                    continue


                # =============================================
                # PALM
                # =============================================

                palm_points = np.array(
                    [
                        points[0],
                        points[5],
                        points[9],
                        points[13],
                        points[17]
                    ],
                    dtype=np.int32
                )


                cv2.fillPoly(
                    hand_mask,
                    [palm_points],
                    255
                )


                # =============================================
                # FINGERS
                # =============================================

                fingers = [

                    [1, 2, 3, 4],

                    [5, 6, 7, 8],

                    [9, 10, 11, 12],

                    [13, 14, 15, 16],

                    [17, 18, 19, 20]

                ]


                for finger in fingers:


                    for i in range(
                        len(finger) - 1
                    ):


                        a = points[
                            finger[i]
                        ]


                        b = points[
                            finger[i + 1]
                        ]


                        thicknesses = [
                            9,
                            7,
                            5
                        ]


                        thickness = (
                            thicknesses[
                                min(
                                    i,
                                    2
                                )
                            ]
                        )


                        cv2.line(
                            hand_mask,
                            a,
                            b,
                            255,
                            thickness,
                            cv2.LINE_AA
                        )


                        cv2.circle(
                            hand_mask,
                            a,
                            thickness // 2,
                            255,
                            -1,
                            cv2.LINE_AA
                        )


                    # =========================================
                    # FINGERTIP
                    # =========================================

                    tip = points[
                        finger[-1]
                    ]


                    cv2.circle(
                        hand_mask,
                        tip,
                        3,
                        255,
                        -1,
                        cv2.LINE_AA
                    )


                # =============================================
                # PALM CONNECTIONS
                # =============================================

                for joint in [
                    5,
                    9,
                    13,
                    17
                ]:


                    cv2.line(
                        hand_mask,
                        points[0],
                        points[joint],
                        255,
                        8,
                        cv2.LINE_AA
                    )


        # ====================================================
        # SMOOTH HAND MASK
        # ====================================================

        hand_mask = cv2.GaussianBlur(
            hand_mask,
            (
                5,
                5
            ),
            0
        )


        # ====================================================
        # COMBINE BODY + HANDS
        # ====================================================

        final_mask = cv2.bitwise_or(
            body_mask,
            hand_mask
        )


        # ====================================================
        # FINAL EDGE SMOOTHING
        # ====================================================

        final_mask = cv2.GaussianBlur(
            final_mask,
            (
                7,
                7
            ),
            0
        )


        final_mask = cv2.morphologyEx(
            final_mask,
            cv2.MORPH_CLOSE,
            np.ones(
                (
                    3,
                    3
                ),
                np.uint8
            )
        )


        # ====================================================
        # BLACK SILHOUETTE ON WHITE
        # ====================================================

        silhouette = np.full_like(
            frame,
            255
        )


        # Use a soft-to-hard transition
        # for smoother projected edges.

        silhouette[
            final_mask > 110
        ] = (
            0,
            0,
            0
        )


        # ====================================================
        # ANIMATION TIME
        # ====================================================

        elapsed = (
            time.monotonic()
            - start_time
        )


        # ====================================================
        # OPENING PROGRESS
        # ====================================================

        progress = min(
            elapsed
            / OPENING_DURATION,
            1.0
        )


        # Smoothstep easing

        eased = (
            progress
            * progress
            * (
                3
                - 2 * progress
            )
        )


        # ====================================================
        # MAXIMUM RADIUS
        # ====================================================

        max_radius = int(
            math.sqrt(
                width * width
                + height * height
            )
        )


        opening_radius = int(
            START_RADIUS
            + (
                max_radius
                - START_RADIUS
            )
            * eased
        )


        # ====================================================
        # CREATE BLACK BACKGROUND
        # ====================================================

        spiral = np.zeros_like(
            frame
        )


        # ====================================================
        # SPIRAL ROTATION
        # ====================================================

        rotation = (
            elapsed
            * ROTATION_SPEED
        )


        # ====================================================
        # DRAW BLADES
        # ====================================================

        for blade in range(
            NUM_BLADES
        ):


            start_angle = (
                blade
                * (
                    2
                    * math.pi
                    / NUM_BLADES
                )
            )


            points = create_blade(
                person_center_x,
                person_center_y,
                start_angle,
                rotation,
                START_RADIUS,
                max_radius * 2,
                BLADE_WIDTH
            )


            cv2.fillPoly(
                spiral,
                [points],
                (
                    255,
                    255,
                    255
                ),
                lineType=cv2.LINE_AA
            )


        # ====================================================
        # WHITE INNER CIRCLE
        # ====================================================

        cv2.circle(
            spiral,
            (
                person_center_x,
                person_center_y
            ),
            opening_radius,
            (
                255,
                255,
                255
            ),
            -1,
            cv2.LINE_AA
        )


        # ====================================================
        # CIRCLE MASK
        # ====================================================

        circle_mask = np.zeros(
            (
                height,
                width
            ),
            dtype=np.uint8
        )


        cv2.circle(
            circle_mask,
            (
                person_center_x,
                person_center_y
            ),
            opening_radius,
            255,
            -1,
            cv2.LINE_AA
        )


        # ====================================================
        # SILHOUETTE INSIDE CIRCLE
        # ====================================================

        person_inside = (
            cv2.bitwise_and(
                final_mask,
                circle_mask
            )
        )


        spiral[
            person_inside > 110
        ] = (
            0,
            0,
            0
        )


        # ====================================================
        # AFTER OPENING
        # ====================================================

        if progress >= 1.0:

            output = silhouette

        else:

            output = spiral


        # ====================================================
        # FINAL DISPLAY SMOOTHING
        # ====================================================

        output = cv2.GaussianBlur(
            output,
            (
                3,
                3
            ),
            0
        )


        # ====================================================
        # FULLSCREEN DISPLAY
        # ====================================================

        cv2.imshow(
            WINDOW_NAME,
            output
        )


        # ====================================================
        # KEYBOARD
        # ====================================================

        key = (
            cv2.waitKey(1)
            & 0xFF
        )


        if key == ord("q"):

            break


# ============================================================
# CLEANUP
# ============================================================

camera.release()

cv2.destroyAllWindows()


if music_enabled:

    try:

        pygame.mixer.music.stop()

        pygame.mixer.quit()

    except:

        pass


print(
    "Bond silhouette stopped."
)