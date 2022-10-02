def stock_availability(boxes, command, *args):
    if command == 'delivery':
        boxes.extend(args)
    elif command == 'sell':
        if not args:
            del boxes[0]
        elif args:
            for arg in args:
                number = isinstance(arg, int)
                if number:
                    n = arg
                    for a in range(n):
                        del boxes[0]
                ordered_boxes = isinstance(arg, str)
                if ordered_boxes:
                    ordered_boxes = arg
                    while ordered_boxes in boxes:
                        boxes.remove(ordered_boxes)

    return boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

