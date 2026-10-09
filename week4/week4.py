import turtle

# for x in range(100):
#     print(f"{x}. We like Python's turtles!")
#
# months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
#
# for month in months:
#     print(f"One of the months of the year is {month}")
#
# list_of_numbers = [12,10,32,3,66,17,42,99,20]
#
# for number in list_of_numbers:
#     print(f"Our number is {number}")
#
# for number in list_of_numbers:
#     print(f"Our number and its square is {number}, {number**2}")
#
#


#sides = int(input("How many sides? "))
#lenght_of_sides = int(input("How long is one edge?"))

leg_amount = int(input("Enter the amount of legs: "))

screen = turtle.Screen()
screen.bgcolor("black")
turtle = turtle.Turtle()
turtle.speed(10)
turtle.color("light green")
#
def new_location(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
#
# for edge in range(3):
#     turtle.forward(100)
#     turtle.left(120)
#
# new_location(-120,0)
#
# for edge in range(4):
#     turtle.forward(100)
#     turtle.left(90)
#
# new_location(120,0)
#
# for edge in range(6):
#     turtle.forward(100)
#     turtle.left(60)
#
# new_location(-320,0)
#
# for edge in range(8):
#     turtle.forward(100)
#     turtle.left(45)



# turtle.begin_fill()
#
# for i in range(sides):
#     turtle.forward(lenght_of_sides)
#     turtle.left(360/sides)
#
# turtle.end_fill()

#A Drunk Pirate
experimental_data = [160, -43, 270, -97, -43, 200, -940, 17, -86]

#
# for x in experimental_data:
#     turtle.left(x%360)
#     turtle.forward(100)

#drawing a star
# for i in range(5):
#     turtle.right(144)
#     turtle.forward(100)
# screen.exitonclick()

# def stamper():
#     turtle.shape("turtle")
#     turtle.penup()
#     turtle.forward(80)
#     turtle.pendown()
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.stamp()
#     turtle.back(100)
#     turtle.left(30)
#     pass
#
# for i in range(12):
#     stamper()
screen.bgcolor("dark gray")

def draw_legs():
    turtle.forward(190)
    turtle.back(190)


for i in range(leg_amount):
    draw_legs()
    turtle.right(360/leg_amount)

turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(0,-80)
turtle.circle(80)
turtle.end_fill()
turtle.penup()
turtle.goto(0,60)
turtle.begin_fill()
turtle.pendown()
turtle.circle(40)
turtle.end_fill()
turtle.penup()
turtle.goto(0,80)





screen.exitonclick()
