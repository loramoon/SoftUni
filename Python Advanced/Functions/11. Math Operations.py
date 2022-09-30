from collections import deque


def math_operations(*args, **kwargs):
    q = deque(args)
    while q:
        element = q.popleft()
        kwargs['a'] += element
        if not q:
            break
        element = q.popleft()
        kwargs['s'] -= element
        if not q:
            break
        element = q.popleft()
        if element != 0:
            kwargs["d"] /= element
        if not q:
            break
        element = q.popleft()
        kwargs["m"] *= element

    sorted_result = [f'{key}: {value:.1f}' for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]
    return '\n'.join(sorted_result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))