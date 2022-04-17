from sys import argv

script_payment, pay_hour, hours, award = argv
pay_hour = float(pay_hour)
hours = float(hours)
award = float(award)

payment = round(pay_hour * hours, 2)
pay_award = round(payment * award * 0.01, 2)
total_pay = payment + pay_award
print(f'Зарплата в час (руб): {pay_hour:.2f}')
print('Отработано часов: ', hours)
print(f'Премия расчитывается из расчета {award} % от выплаты')
print('-' * 50)
print(f'Зарплата сотрудника составляет: {payment:.2f} руб.')
print(f'Премиальная выплата составляет: {pay_award:.2f} руб.')
print(f'Всего к выплате: {total_pay:.2f} руб.')
