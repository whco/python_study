def add_many(*args):
    result = 0
    print(type(args))
    for arg in args:
        result += arg
    print(result)
    return result


def print_kwargs(**kwargs):
    print(kwargs)


def args_practice():
    # add_many(1,2,3,4,5,6,)
    print_kwargs(3)


if __name__ == '__main__':
    args_practice()
