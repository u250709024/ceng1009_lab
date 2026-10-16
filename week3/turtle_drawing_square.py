import turtle
import random

ok = turtle.Turtle()
ok.speed(50)

ok.forward(250)
ok.right(90)
ok.forward(250)
ok.right(90)
ok.forward(250)
ok.right(90)
ok.forward(250)
ok.right(45)
ok.forward(250)

for x in range(0,3):
    ok.forward(200)
    ok.right(175)

for idil in range(3, 30, 2):
    print(f"idilin {idil} tane elması var")

turtle.done()

