def fill_the_box(h, le, w, *args):
    volume = h*le*w
    cubes_left = 0
    for i in list(args):
        if i != "Finish":
            volume -= i
        else:
            if volume>0:
                return f"There is free space in the box. You could put {volume} more cubes."
            else:
                return f"No more free space! You have {volume*-1} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))