def example1():
    list1 = [1, 2, 3, 4, 5, 9, 11]
    list2 = [4, 5]

    new_list = [item for item in list1 if item in list2]

    print(new_list)

def example2():
    list1 = [1, 2, 3, 4, 5, 9, 11]
    list2 = [4, 5]

    new_list = [item for item in list1 if item not in list2]

    print(new_list)

def example3():
    list1 = [1, 2, 3, 4, 5, 9, 11]
    new_list = [item for item in list1 if item%2 == 0]

    print(new_list)

example1()
example2()
example3()