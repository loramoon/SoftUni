def vowel_filter(func_ref):
    vowels = 'aoeiyu'

    def wrapper():
        result = func_ref()
        return [x for x in result if x in vowels]

    return wrapper
