# import turtle
# import random
# myPen = turtle.Turtle()
# myPen.shape("turtle")
# myPen.speed(10)

# window = turtle.Screen()

# def logo():
#   def corner(turtle):
#   for x in range(0, 6):
#     turtle.left(15)
#     turtle.forward(2)

# def cornered_box(turtle, x1, y1, x2, y2, letter):
#   turtle.penup()
#   turtle.goto(x1, y1)
#   turtle.pendown()
#   turtle.color("black")
#   turtle.fillcolor("white")
#   turtle.begin_fill()
#   for x in range(0, 4):
#     turtle.forward(40)
#     corner(turtle)
#   turtle.end_fill()
#   turtle.penup()
#   turtle.goto(x2, y2)
#   turtle.color("black")
#   turtle.write(letter, None, None, "28pt bold")

# cornered_box(myPen, -40, 20, -35, 35, "v")
# cornered_box(myPen, 25, 20, 30, 35, "i")
# cornered_box(myPen, -40, -45, -35, -30, "b")
# cornered_box(myPen, 25, -45, 30, -30, "h")




# myPen.goto(10, 105)

# for x in range(0, 100):
#   myPen.color("#%06x" % random.randint(0, 2**24 - 1))
# myPen.color("white")