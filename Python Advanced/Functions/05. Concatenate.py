def concatenate(*args, **kwargs):
    text = ''
    for i in args:
        text += i
    for k, v in kwargs.items():
        if k in text:
            text=text.replace(k, v)
    return text


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))