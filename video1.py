from vpython import *
from math import sin, cos, pi

# Puts X number of spheres in a circle, equally spaced
# (adjust SPHERES constant)
# rays are tangent to the circle

SPHERES = 3
SPHERE_RADIUS = 1
CIRCLE_RADIUS = 2
AXIS_LENGTH = 2
CLOCKWISE = False
ANGLE_OFFSET = -10

for i in range(SPHERES):
    angle = i * 2 * pi / SPHERES + ANGLE_OFFSET
    position = vector(
        sin(angle) * CIRCLE_RADIUS,
        cos(angle) * CIRCLE_RADIUS,
        0
    )
    sphere(
        pos = position,
        radius = SPHERE_RADIUS,
        color = color.green
    )
    arrow(
        pos = position,
        axis = vector(
            sin(angle + (1 if CLOCKWISE else -1) * pi / 2) * AXIS_LENGTH,
            cos(angle + (1 if CLOCKWISE else -1) * pi / 2) * AXIS_LENGTH,
            0
        ),
        color = color.red
    )
