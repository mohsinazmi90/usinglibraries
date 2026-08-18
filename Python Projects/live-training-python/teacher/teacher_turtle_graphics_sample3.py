import turtle

screen = turtle.Screen()
screen.title("Turtle Sample")
screen.bgcolor("silver")

pen = turtle.Turtle()
pen.speed(0)

colors = ["red", "orange", "Indigo","gold", "green", "blue", "grey", "purple"]
for i in range(120):
    pen.color(colors[i % len(colors)])
    pen.forward(i * 2)
    pen.left(59)

turtle.done()