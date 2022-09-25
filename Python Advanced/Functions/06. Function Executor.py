
def func_executor(*args):
    result = []
    for func_ref, func_params in args:
        func_result = func_ref(*func_params)
        result.append(f'{func_ref.__name__} - {func_result}')
    return '\n'.join(result)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

