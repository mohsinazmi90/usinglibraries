import turtle
# import tkinter as TK

# 1. SCREEN SETUP
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Graphics Basics")
screen.bgcolor("#F0F4F8")

# 2. CREATE TURTLE INSTANCE
t = turtle.Turtle()
t.shape("turtle")  # OPTIONS: 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
t.color("#1E293B") # <- PEN COLOR
t.pensize(2)
t.speed(3) # SPEED FROM 1 (Slowest) TO 10 (Fastest), 0 MEANS NO ANIMATIONS (Instant)

# 3. PREVENT WINDOW FROM CLOSING IMMEDIATELY
screen.mainloop()
turtle.done()