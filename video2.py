from vpython import *

SPHERE_RADIUS = 0.5
SPHERE_COLOR = color.green
VECTOR_COLOR = color.red

sphere_a = sphere(
	pos = vector(-1, -1, 0),
	radius = SPHERE_RADIUS,
	color = SPHERE_COLOR
)
sphere_b = sphere(
	pos = vector(-1, 1, 0),
	radius = SPHERE_RADIUS,
	color = SPHERE_COLOR
)
sphere_c = sphere(
	pos = vector(1, 0, 0),
	radius = SPHERE_RADIUS,
	color = SPHERE_COLOR
)
vector_ab = arrow(
	pos = sphere_a.pos,
	axis = sphere_b.pos - sphere_a.pos,
	color = VECTOR_COLOR
)
vector_bc = arrow(
	pos = sphere_b.pos,
	axis = sphere_c.pos - sphere_b.pos,
	color = VECTOR_COLOR
)
vector_ca = arrow(
	pos = sphere_c.pos,
	axis = sphere_a.pos - sphere_c.pos,
	color = VECTOR_COLOR
)