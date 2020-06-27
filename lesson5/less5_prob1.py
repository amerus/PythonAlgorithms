'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
'''

from collections import defaultdict

number_of_companies = input('Введите число предприятий:\t')
if number_of_companies.isdigit():
    number_of_companies = int(number_of_companies)

company_inventory = []

for i in range(number_of_companies):
    company_name = input('Название предприятия:\t')
    ind_company = [company_name]
    for j in range(1, 5):
        j = input('Введите прибыль за квартал:\t')
        if j.isdigit():
            j = float(j)
        ind_company.append(j)
    company_inventory.append(tuple(ind_company))

total_companies = len(company_inventory)
total_profit = 0

by_company_name = defaultdict(list)

for name, q1, q2, q3, q4 in company_inventory:
    by_company_name[name].extend([q1, q2, q3, q4, sum([q1, q2, q3, q4])])
    total_profit += by_company_name[name][-1]

average_profit = total_profit/total_companies

for item in by_company_name.items():
    if item[1][-1] > average_profit:
        print(f"Фирма {item[0]} принесла {item[1][-1]}, что больше среднего значения {average_profit:.02f}")
    elif item[1][-1] < average_profit:
        print(f"Фирма {item[0]} принесла {item[1][-1]}, что меньше среднего значения {average_profit:.02f}")
