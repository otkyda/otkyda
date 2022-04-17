

first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
second_list = [n for i, n in enumerate(first_list) if i != 0 and n > first_list[i -1]]
print(second_list)
