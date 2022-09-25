# commodity = input()
# commodity_list = []
#
# while commodity!="stop":
#     commodity_list.append(commodity)
#     commodity = input()
#
# my_dict = {}
#
# for i in range (0, len(commodity_list), 2):
#     key = commodity_list[i]
#     quantity = int(commodity_list[i+1])
#     if key not in my_dict.keys():
#         my_dict[key] = 0
#     my_dict[key] += quantity
#
# for key, quantity in my_dict.items():
#     print(f"{key} -> {quantity}")

def miner_task():
    items_dict = {}

    while True:
        resource = input()

        if resource == "stop":
            break
        quantity = int(input())

        if resource not in items_dict:
            items_dict[resource] = quantity
        else:
            items_dict[resource] += quantity

    for key, value in items_dict.items():
        print(f"{key} -> {value}")

miner_task()