import turtle

scr = turtle.Screen()
turt = turtle.Turtle()
scr.bgcolor("black")
turt.color("#00FF41")
#turtle.tracer(0)
turt.fillcolor("red")
turt.speed(10)

#Write a function which is given an exam mark, and it returns a string — the grade for that mark — according to this scheme:

def grade(note:float):
    if note >= 90: return "A"
    elif note >= 80: return "B"
    elif note >= 70: return "C"
    elif note >= 60: return "D"
    else: return "F"

print(grade(80))

#Modify the turtle bar chart program from the previous chapter so that the bar for any value of 200 or more is filled with red, values between [100 and 200) are filled yellow, and bars representing values less than 100 are filled green.

points = [48,117,200,240,160,260,-220,98,-155,70,11,228,-115]

def turtle_bar_chart(points:points):
    chart_lenght = 300
    def bars(n,lenght):
        color = ""
        def colors():
            if abs(lenght) >= 200:
                return "red"
            elif abs(lenght) >= 100:
                return "yellow"
            else:
                return "green"

        turt.fillcolor(colors())
        turt.begin_fill()
        if lenght < 0:
            turt.write(f"{lenght}")
        turt.left(90)
        turt.forward(lenght)
        turt.right(90)
        if lenght >= 0:
            turt.write(f"{lenght}")
        turt.forward(chart_lenght / len(points))
        turt.right(90)
        turt.forward(lenght)
        turt.right(90)
        turt.forward(chart_lenght / len(points))
        turt.end_fill()
        turt.right(180)
        turt.forward(chart_lenght / len(points))
    for i in points:
        bars(points,i)


#Write a function findHypot. The function will be given the length of two sides of a right-angled triangle and it should return the length of the hypotenuse. (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)

def findHypot(x,y):
    hypot = x**2 + y**2
    hypot = hypot ** 0.5
    return round(hypot, 5)

print(findHypot(7,24))
#turtle_bar_chart(points)
scr.exitonclick()

