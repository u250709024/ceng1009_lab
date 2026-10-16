import math

print("circumference calculator")

radius = float(input("Enter radius: "))
circumference = 2 * 3.14 * radius
real_circumference = 2 * math.pi * radius
print(f"The circumference is  = {round(circumference, 3)}, real circumference = {round(real_circumference, 8)}")

