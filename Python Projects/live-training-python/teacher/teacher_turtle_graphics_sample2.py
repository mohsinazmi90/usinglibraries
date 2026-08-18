# import turtle
# import math

# # 1. SCREEN SETUP
# screen = turtle.Screen()
# screen.bgcolor("#0B0F19")
# screen.title("Parametric Heart Animation")
# screen.setup(width=700, height=700)
# screen.tracer(2) # SPEEDS UP RENDERING WHILE KEEPING ANIMATION VISIBLE

# # 2. TURTLE SETUP
# t = turtle.Turtle()
# t.hideturtle() # HIDES THE TURTLE
# t.speed(0) # 0 MEANS NO ANIMATIONS (Instant)
# t.pensize(2)

# # 3. CREATE FUNCTION FOR HEART
# def heart_x(t):
#     return 16 * (math.sin(t) ** 3)

# def heart_y(t):
#     return (
#         13 * math.cos(t)
#         - 5 * math.cos(2 * t)
#         - 2 * math.cos(3 * t)
#         - math.cos(4 * t)
#     )

# # 3. DRAW EXPANDING, LAYER LOW LINES
# scale = 14
# t.penup()

# for i in range(1, 16):
#     current_scale = scale * (i / 15)
#     # GRADIENT FROM DARK MAGENTO TO VIVID RED/PINK
#     color_val = (0.2 + 0.8 * (i / 15), 0.05 * (i / 15))
#     t.pencolor(color_val)
    
# # 4. TRACE FULL PARAMETER
# t.penup()
# for angle in range(0, 360, 2):
#     rad = math.radians(angle)
#     x = heart_x(rad) * current_scale
#     y = heart_y(rad) * current_scale

# t.goto(x, y)
# t.pendown()

# # 4. PREVENT WINDOW FROM CLOSING IMMEDIATELY
# # screen.mainloop()
# turtle.done()

import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("#0b0f19")
screen.title("Parametric Heart Animation")
screen.setup(width=700, height=700)
screen.tracer(2)  # Speeds up rendering while keeping animation visible

# Turtle setup
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

def heart_x(t):
    return 16 * (math.sin(t) ** 3)

def heart_y(t):
    return (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )

# Draw expanding, layered glow lines
scale = 14
t.penup()

for i in range(1, 16):
    current_scale = scale * (i / 15)
    # Gradient from dark magenta to vivid red/pink
    color_val = (0.2 + 0.8 * (i / 15), 0.05, 0.3 + 0.5 * (i / 15))
    t.pencolor(color_val)
    
    # Trace full perimeter
    t.penup()
    for angle in range(0, 360, 2):
        rad = math.radians(angle)
        x = heart_x(rad) * current_scale
        y = heart_y(rad) * current_scale
        
        t.goto(x, y)
        t.pendown()

turtle.done()