import math
import turtle

# --- Screen Setup ---
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)  # Turn off automatic animation for smooth frame rendering

t = turtle.Turtle()
t.hideturtle()
t.pensize(2)

# --- Define 4D Tesseract Vertices (16 points in 4D space) ---
vertices_4d = []
for x in [-1, 1]:
    for y in [-1, 1]:
        for z in [-1, 1]:
            for w in [-1, 1]:
                vertices_4d.append([x, y, z, w])

# --- Define Edges (Connect vertices that differ by only 1 coordinate) ---
edges = []
for i in range(len(vertices_4d)):
    for j in range(i + 1, len(vertices_4d)):
        # If the points differ in only 1 dimension out of 4, they form an edge
        if sum(1 for k in range(4) if vertices_4d[i][k] != vertices_4d[j][k]) == 1:
            edges.append((i, j))

# --- Rotation Variables ---
angle_xy = 0
angle_zw = 0
angle_xz = 0

screen.colormode(255)


def rotate_4d(point, a_xy, a_zw, a_xz):
    x, y, z, w = point

    # Rotate in XY plane
    x1 = x * math.cos(a_xy) - y * math.sin(a_xy)
    y1 = x * math.sin(a_xy) + y * math.cos(a_xy)

    # Rotate in ZW plane
    z1 = z * math.cos(a_zw) - w * math.sin(a_zw)
    w1 = z * math.sin(a_zw) + w * math.cos(a_zw)

    # Rotate in XZ plane
    x2 = x1 * math.cos(a_xz) - z1 * math.sin(a_xz)
    z2 = x1 * math.sin(a_xz) + z1 * math.cos(a_xz)

    return [x2, y1, z2, w1]


def project_4d_to_2d(point, distance_4d=3, distance_3d=4, scale=180):
    x, y, z, w = point

    # 4D to 3D perspective projection
    w_factor = 1 / (distance_4d - w)
    x3 = x * w_factor
    y3 = y * w_factor
    z3 = z * w_factor

    # 3D to 2D perspective projection
    z_factor = 1 / (distance_3d - z3)
    x2d = x3 * z_factor * scale
    y2d = y3 * z_factor * scale

    return x2d, y2d


# --- Animation Loop ---
frame = 0
try:
    while True:
        t.clear()

        # Dynamic color cycling based on frame count
        r = int((math.sin(frame * 0.03) + 1) * 127)
        g = int((math.sin(frame * 0.03 + 2) + 1) * 127)
        b = int((math.sin(frame * 0.03 + 4) + 1) * 127)
        t.color(r, g, b)

        # Rotate and project all vertices
        projected_points = []
        for v in vertices_4d:
            rotated = rotate_4d(v, angle_xy, angle_zw, angle_xz)
            p2d = project_4d_to_2d(rotated)
            projected_points.append(p2d)

        # Draw all connecting edges
        for edge in edges:
            p1 = projected_points[edge[0]]
            p2 = projected_points[edge[1]]

            t.penup()
            t.goto(p1[0], p1[1])
            t.pendown()
            t.goto(p2[0], p2[1])

        screen.update()

        # Update rotation angles for continuous animation
        angle_xy += 0.02
        angle_zw += 0.015
        angle_xz += 0.01
        frame += 1

except turtle.TerminatorError:
    pass