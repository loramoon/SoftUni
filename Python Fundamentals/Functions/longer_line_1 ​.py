import math

def get_distance(_x1, _y1, _x2, _y2, _x11, _y11, _x22, _y22):
    return math.sqrt(math.pow(_x2 - _x1, 2.0) + math.pow(_y2 - _y1, 2.0) + math.pow(_x22 - _x11, 2.0) + math.pow(_y22 - _y11, 2.0))

x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x11 = math.floor(float(input()))
y11 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))
x22 = math.floor(float(input()))
y22 = math.floor(float(input()))

dist1 = get_distance(x1, y1, 0, 0, 0, 0, 0, 0)
dist11 = get_distance(x11, y11, 0, 0, 0, 0, 0, 0)
dist2 = get_distance(x2, y2, 0, 0, 0, 0, 0, 0)
dist22 = get_distance(x22, y22, 0, 0, 0, 0, 0, 0)

if dist1 >= dist2:
    if dist1 <= dist11:
        print(f"({x1}, {y1})({x11}, {y11})")
    else:
        print(f"({x11}, {y11})({x1}, {y1})")
else:
    if dist2 <= dist22:
        print(f"({x2}, {y2})({x22}, {y22})")
    else:
        print(f"({x22}, {y22})({x2}, {y2})")