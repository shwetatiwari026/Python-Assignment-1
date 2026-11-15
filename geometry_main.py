from circle import area as circle_area
from rectangle import area as rectangle_area

radius = float(input("Enter circle radius: "))
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

if radius < 0 or length < 0 or width < 0:
    print("Measurements cannot be negative.")
else:
    print("Area of circle:", round(circle_area(radius), 2))
    print("Area of rectangle:", rectangle_area(length, width))
