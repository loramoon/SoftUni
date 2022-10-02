from collections import deque


def flights(*args):
    travel_dict = {}
    args = deque(args)
    while args:
        arg_1 = args.popleft()
        if arg_1 == 'Finish':
            break
        destination = isinstance(arg_1, str)
        if destination:
            if arg_1 not in travel_dict:
                travel_dict[arg_1] = 0
            arg_2 = args.popleft()
            passengers = isinstance(arg_2, int)
            if passengers:
                travel_dict[arg_1] += arg_2

    return travel_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
