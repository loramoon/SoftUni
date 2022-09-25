# import math
#
# def get_distance(_x1, _y1, _x2, _y2):
#     return math.sqrt(math.pow(_x2 - _x1, 2.0) + math.pow(_y2 - _y1, 2.0))
#
# x1 = math.floor(float(input()))
# y1 = math.floor(float(input()))
# x2 = math.floor(float(input()))
# y2 = math.floor(float(input()))
#
# dist1 = get_distance(x1, y1, 0, 0)
# dist2 = get_distance(x2, y2, 0, 0)
#
# if dist1 <= dist2:
#     print(f"({x1}, {y1})")
# else:
#     print(f"({x2}, {y2})")

''''You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate
lines. Write a function that prints the point which is closest to the center of the coordinate system (0, 0)
in the format: "({X}, {Y})"
If the points are at the same distance from the center, print only the first one.
The resulting coordinates must be formatted to the lower integer.
'''

import math

def get_hipotenuse(num1, num2):
    x = math.pow(num1, 2)
    y = math.pow(num2, 2)
    return math.sqrt(x + y)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

z1 = get_hipotenuse(x1, y1)
z2 = get_hipotenuse(x2, y2)
if z1 <= z2:
    print(f"({math.floor(x1)}, {math.floor(y1)})")
else:
    print(f"({math.floor(x2)}, {math.floor(y2)})")