def add_nums(a, b):
    if isinstance(a, (int, float, complex)):
        if isinstance(b, (int, float, complex)):
            return a + b
    raise ValueError('Not compatible for addition')
