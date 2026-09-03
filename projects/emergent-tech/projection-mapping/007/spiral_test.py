import cv2
import numpy as np
import math
import time


# ============================================================
# SETTINGS
# ============================================================

WIDTH = 1280
HEIGHT = 720

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2


# ============================================================
# SPIRAL
# ============================================================

NUM_BLADES = 7

# Rotation speed
ROTATION_SPEED = 0.7

# Starting size of the center circle
START_RADIUS = 80

# Maximum size of the opening
MAX_RADIUS = 900

# Speed of the opening
# Smaller number = slower opening
OPEN_SPEED = 30

# Thickness of the blade at the outside
BLADE_WIDTH = 110

# How much the blade curves
SPIRAL_CURVE = 100


# ============================================================
# CREATE ONE TAPERED SPIRAL BLADE
# ============================================================

def create_blade(
    center_x,
    center_y,
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

    for i in range(point_count):

        t = i / (point_count - 1)

        # Radius grows from center toward outside
        radius = (
            inner_radius
            + (outer_radius - inner_radius) * t
        )

        # Spiral curve
        angle = (
            start_angle
            + rotation
            + t * math.radians(SPIRAL_CURVE)
        )

        # Strong taper:
        # extremely thin near center
        # thick toward outside
        local_width = width * (t ** 1.8)

        # Perpendicular direction to the curve
        offset_angle = angle + math.pi / 2

        x = (
            center_x
            + radius * math.cos(angle)
            + local_width * math.cos(offset_angle)
        )

        y = (
            center_y
            + radius * math.sin(angle)
            + local_width * math.sin(offset_angle)
        )

        points.append(
            (int(x), int(y))
        )


    # ========================================================
    # SECOND EDGE
    # ========================================================

    for i in range(point_count - 1, -1, -1):

        t = i / (point_count - 1)

        radius = (
            inner_radius
            + (outer_radius - inner_radius) * t
        )

        angle = (
            start_angle
            + rotation
            + t * math.radians(SPIRAL_CURVE)
        )

        # Same strong taper
        local_width = width * (t ** 1.8)

        offset_angle = angle - math.pi / 2

        x = (
            center_x
            + radius * math.cos(angle)
            + local_width * math.cos(offset_angle)
        )

        y = (
            center_y
            + radius * math.sin(angle)
            + local_width * math.sin(offset_angle)
        )

        points.append(
            (int(x), int(y))
        )


    return np.array(
        points,
        dtype=np.int32
    )


# ============================================================
# MAIN
# ============================================================

print("Spiral door test started.")
print("Press Q to quit.")


start_time = time.monotonic()


while True:

    # ========================================================
    # TIME
    # ========================================================

    elapsed = (
        time.monotonic()
        - start_time
    )


    # ========================================================
    # BLACK BACKGROUND
    # ========================================================

    canvas = np.zeros(
        (HEIGHT, WIDTH, 3),
        dtype=np.uint8
    )


    # ========================================================
    # ROTATION
    # ========================================================

    rotation = (
        elapsed
        * ROTATION_SPEED
    )


    # ========================================================
    # EXPANDING WHITE CIRCLE
    # ========================================================

    opening_radius = (
        START_RADIUS
        + elapsed * OPEN_SPEED
    )

    opening_radius = min(
        opening_radius,
        MAX_RADIUS
    )


    # ========================================================
    # WHITE SPIRAL BLADES
    # ========================================================

    for blade in range(NUM_BLADES):

        start_angle = (
            blade
            * (2 * math.pi / NUM_BLADES)
        )


        points = create_blade(
            CENTER_X,
            CENTER_Y,
            start_angle,
            rotation,
            opening_radius,
            MAX_RADIUS,
            BLADE_WIDTH
        )


        cv2.fillPoly(
            canvas,
            [points],
            (255, 255, 255),
            lineType=cv2.LINE_AA
        )


    # ========================================================
    # WHITE CIRCULAR OPENING
    #
    # IMPORTANT:
    # This is WHITE because this is where the
    # BLACK LIVE SILHOUETTE will eventually appear.
    # ========================================================

    cv2.circle(
        canvas,
        (CENTER_X, CENTER_Y),
        int(opening_radius),
        (255, 255, 255),
        -1,
        cv2.LINE_AA
    )


    # ========================================================
    # DISPLAY
    # ========================================================

    cv2.imshow(
        "Spiral Door Test",
        canvas
    )


    # ========================================================
    # QUIT
    # ========================================================

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break


# ============================================================
# CLEAN UP
# ============================================================

cv2.destroyAllWindows()