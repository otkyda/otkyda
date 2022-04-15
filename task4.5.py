from functools import reduce

numbers = list(range(100,1001))

def my_func(prev_el, el):
    return prev_el * el 

print(reduce(my_func, numbers))