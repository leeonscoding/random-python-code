def way1():
    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7]
    list4 = [8, 9, 10]

    new_list = list1 + list2 + list3 + list4

    print(new_list)

def way2():
    list1 = [1, 2, 3]
    list2 = [4, 5]

    list1.extend(list2)

    print(list1)

way1()
way2()