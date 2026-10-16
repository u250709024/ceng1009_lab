import random
import math
import turtle
# 1  Use a for statement to print 10 random numbers.
for i in range(10):
    print(f"Random number: {random.random()}")

# 2  Repeat the above exercise but this time print 10 random numbers between 25 and 35, inclusive.

for i in range(10):
    print(f"Random number between 25 and 35: {random.randint(25, 35)}")

# 3  The Pythagorean Theorem tells us that the length of the hypotenuse of a right triangle is related to the lengths of the other two sides. Look through the “math” module and see if you can find a function that will compute this relationship for you. Once you find it, write a short program to try it out.

lenght = random.randint(1,50)
width = random.randint(1,50)
hypothenuse = math.hypot(width,lenght)
print(round(hypothenuse, 3))

# 4  Write a function areaOfCircle(r) which returns the area of a circle of radius r. Make sure you use the math module in your solution.

def area_of_circle(radius:int):
    return math.pi * radius ** 2

print(area_of_circle(random.randint(1,50)))

# 5  Write a non-fruitful function to draw a five pointed star, where the length of each side is 100 units.

scr = turtle.Screen()
trt = turtle.Turtle()
scr.bgcolor("black")
trt.color("#20C20E")

def turtle_star():
    for i in range(5):
        trt.forward(100)
        trt.right(144)

#Use the drawsquare function we wrote in this chapter in a program to draw the image shown below. Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last square when the program ends.)

def turtle_squares1():
    for i in range(1,6):
        for j in range(4):
            trt.forward(20)
            trt.right(90)
        trt.penup()
        trt.goto((i*40),0)
        print(i*40)
        trt.pendown()

#Write a program to draw this. Assume the innermost square is 20 units per side, and each successive square is 20 units bigger, per side, than the one inside it.

def turtle_squares2():
    for i in range(1,6):
        for j in range(4):
            trt.forward(20*i)
            trt.right(90)

        trt.penup()
        trt.goto(-(i*10),(i*10))
        trt.pendown()


#Son üç soruyu buradan istediğinizin commentini açarak başlatabilirsiniz
#turtle_star()
#turtle_squares1()
#turtle_squares2()

scr.exitonclick()