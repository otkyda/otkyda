from random import randint
import json

index = randint(1, 100)
num = 0
print('число', index)
count_list = []
while num <= index:
    count = randint(1, 1000)
    num = num + 1
    count_list.append(count)
print(count_list)

out_f = open('some_list.txt', 'w+', encoding='utf-8')
out_f.write(' '.join(map(str, count_list)))
out_f.seek(0)
print(sum(map(int, out_f.readline().split())))
out_f.close()
