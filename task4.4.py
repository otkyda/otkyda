from collections import Counter

first_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

out_list = [i for i,v in Counter(first_list).items() if v==1]

print(out_list)
