def start_spring(**kwargs):
    new_list = {}
    for k, v in kwargs.items():
        if v not in new_list.keys():
            new_list[v] = []
        new_list[v].append(k)

    result = ''
    sorted_new_list = sorted(new_list.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple_ in sorted_new_list:
        type_object = tuple_[0]
        list_of_objects = tuple_[1]
        sorted_list_of_objects = sorted(list_of_objects)
        result += f"{type_object}:\n"
        for obj in sorted_list_of_objects:
            result += f"-{obj}\n"
    return result.strip()


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

