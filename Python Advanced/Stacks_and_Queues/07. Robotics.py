robots = [x for x in input().split(';')]
robots_dict = {}
starting_time = [int(x) for x in input().split(':')]
commands = input()
production = []

for robot in range(len(robots)):
    k, v = robots[robot].split('-')
    v = int(v)
    robots_dict[k] = v

while commands != 'End':
    production.append(commands)
    commands = input()

for robot, time in robots_dict.items():
    print(starting_time)
    starting_time[2] +=  robots_dict[robot]

print(robots_dict)
print((starting_time))
