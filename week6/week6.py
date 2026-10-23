import turtle

#Write a non-fruitful function drawPoly(someturtle, somesides, somesize) which makes a turtle draw a regular polygon. When called with drawPoly(tess, 8, 50), it will draw a shape like this:

screen = turtle.Screen()


drawer = turtle.Turtle()
drawer.shape('arrow')
drawer.color('blue')
drawer.speed(11)


def draw_poly(turt, sides, size):
    for i in range(sides):
        turt.forward(size)
        turt.left(360/sides)
    pass

#draw_poly(drawer, 10, 20)


#Draw this pretty pattern.

def draw_prettysquare(turt, amount, size):
    for i in range(amount):
        for x in range(4):
            turt.forward(size)
            turt.left(90)
        turt.left(360/amount)
    pass

#draw_prettysquare(drawer, 20, 100)

#The two spirals in this picture differ only by the turn angle. Draw both

def draw_spiral(turt, amount, size, angle, startx,starty):
    turt.penup()
    turt.goto(startx,starty)
    turt.pendown()
    for i in range(amount*4):
        turt.forward(size*i +5)
        turt.left(angle)

    pass

#draw_spiral(drawer, 20,3,90,-200,0)
#draw_spiral(drawer, 20,3,89,+200,0)

#Write a non-fruitful function drawEquitriangle(someturtle, somesize) which calls drawPoly from the previous question to have its turtle draw a equilateral triangle

def draw_equitriangle(turt, size,):
    draw_poly(turt, 3, size)

    pass

#draw_equitriangle(drawer, 20)

#Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units, turn right by 144, put the pen down, and draw the next star. You’ll get something like this (note that you will need to move to the left before drawing your first star in order to fit everything in the window):
def draw_star(turt, size,startx,starty):
    turt.penup()
    turt.goto(startx,starty)
    turt.pendown()
    for x in range(5):
        for i in range(5):
            turt.forward(size)
            turt.right(144)
        turt.penup()
        turt.forward(350)
        turt.right(144)
        turt.pendown()


    pass

#draw_star(drawer,100,-100,0)

#
def draw_sprite(turt, num_legs, leg_length):

    turn_angle = 360 / num_legs

    turt.dot(15)

    for _ in range(num_legs):
        turt.forward(leg_length)
        turt.backward(leg_length)
        turt.right(turn_angle)

draw_sprite(drawer, 15, 120)

screen.exitonclick()

