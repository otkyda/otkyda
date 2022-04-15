def first_list(*args):
    first_list = [*args]
    second_list = []
        for i in range(len(first_list[:-2])):
        if first_list[i + 1] > first_list[i]:
            second_list.append(first_list[i + 1])
    print(second_list)

first_list(300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55)