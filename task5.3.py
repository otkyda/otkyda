out_f = open('for task 3.txt', 'r', encoding='utf-8')
pay_list = []
number = 0
fond = 0
for line in out_f:
    name, payment = (i for i in line.split())
    payment = float(payment)
    number = number + 1
    fond = fond + payment
    if payment < 20000:
        print(name)
aver = round(fond/number, 2)
print(f'Средняя зарплата: {aver}')
out_f.close()
