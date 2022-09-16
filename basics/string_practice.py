def return_type_test(n):
    s = "abcd"
    s.isdigit()
    if n == 1:
        return 1
    return "hi"


def string_practice():
    x = "abcd"
    enumerate(x)
    s = "try hello  world   ".split(' ')
    x.replace('t', 's')
    print(s)

    # return_type_test(1)

if __name__ == '__main__':
    print(string_practice())
