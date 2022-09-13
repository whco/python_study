def list_practice():
    lst = [1, 2, 3, 4]
    lst.pop()
    lst.extend([5,6])
    print(lst)

    lst2 = [c for c in '가나다라']\
        .extend([1,2])
    # lst2.extend([1,2])
    print(lst2)



if __name__ == '__main__':
    list_practice()
