from itertools import cycle

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

for el in cycle(my_list) :
    if el == 11 :
        break
    print(el)
 