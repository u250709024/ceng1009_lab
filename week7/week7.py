import turtle

scr = turtle.Screen()
turt = turtle.Turtle()
scr.bgcolor("black")
turt.color("#00FF41")
#turtle.tracer(0)
turt.fillcolor("red")
turt.speed(10)


#Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n. So sumTo(10) would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2
def sumTo(n):
    summary = n * (n+1)/2
    return int(summary)

#Extend the star function to draw an n pointed star. (Hint: n must be an odd number greater or equal to 3)

def n_point_star(n):
    if n%2 == 0 or n < 3:
        print("n must be odd number and greater or equal to 3")
        return
    else:
        angle = 180 - (180/n)
        for i in range(n):
            turt.forward(200)
            turt.left(angle)

#Rewrite the function sumTo(n) that returns the sum of all integer numbers up to and including n. This time use the accumulator pattern.

def sumToAccumulator(n):
    if type(n) == int and n > 0:
        summary = 0
        for i in range(n+1):
            summary += i

    return summary

#Write a function called mySqrt that will approximate the square root of a number, call it n, by using Newton’s algorithm. Newton’s approach is an iterative guessing algorithm where the initial guess is n/2 and each subsequent guess is computed using the formula: newguess = (1/2) * (oldguess + (n/oldguess))

def mySqrt(n):

    oldguess = n/2

    while True:
        newguess = (1/2) * (oldguess + (n/oldguess))

        if abs(newguess - oldguess) < 0.001:
            return newguess

        oldguess = newguess

#5Write a function called fancySquare that will draw a square with fancy corners (sprites on the corners). You should implement and use the drawSprite function from above. For an even more interesting look, how about adding small triangles to the ends of the sprite legs

def fancySquare():
    def drawtriangle():
        for i in range(3):
            turt.right(30)
            turt.forward(40)
            turt.left(150)
    def drawsprite(n):
        for i in range(n):
            turt.forward(70)
            turt.begin_fill()
            drawtriangle()
            turt.end_fill()
            turt.backward(70)
            turt.right(360/n)
    def drawsquare():
        for i in range(4):
            turt.forward(250)
            drawsprite(8)
            turt.right(90)
    drawsquare()



#6Write a function that takes a number and returns whether it is positive, negative, or zero.

def iswhat(n):
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    else:
        return "positive"

#There was a whole program in A Turtle Bar Chart to create a bar chart with specific data. Creating a bar chart is a useful idea in general. Write a non-fruitful function called barChart, that takes the numeric list of data as a parameter, and draws the bar chart. Write a full program calling this function. The current version of the drawBar function unfortunately draws the top of the bar through the bottom of the label. A nice elaboration is to make the label appear completely above the top line. To keep the spacing consistent you might pass an extra parameter to drawBar for the distance to move up. For the barChart function make that parameter be some small fraction of maxheight+border. The fill action makes this modification particularly tricky: You will want to move past the top of the bar and write before or after drawing and filling the bar

points = [48,117,200,240,160,260,220,98,155,70,11,228,115]

def turtle_bar_chart(points:points):
    chart_lenght = 300
    def bars(n,lenght):
        turt.begin_fill()
        turt.left(90)
        turt.forward(lenght)
        turt.right(90)
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

#turtle_bar_chart(points)
fancySquare()
#n_point_star(13)
scr.exitonclick()
