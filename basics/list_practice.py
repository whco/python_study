def zip_prac():
    alist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(type(zip(alist)))
    print(list(zip(alist)))


def list_practice():
    # func_prac()
    # list_comp_prac()
    # map_prac()
    zip_prac()

def map_prac():
    lst = [1.2, 2, 3, 4]
    print(type(map(int, lst)))


def list_comp_prac():
    lst2 = [c for c in '가나다라'] \
        .extend([1, 2])
    # lst2.extend([1,2])
    print(lst2)


def func_prac():
    lst = [1, 2, 3, 4]
    lst.pop()
    lst.extend([5, 6])
    print(lst)


if __name__ == '__main__':
    list_practice()
