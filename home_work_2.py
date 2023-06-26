'''Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии'''

name = ['Денис', 'Марина']
rate = [2000, 5000]
percent = ['10.25%', '10.25%']

def get_salary(name: list[str], rate: list[float], percent: list[str]) -> dict[str: float]:
    return {name: rate / 100 * percent for name, rate, percent in zip(name, rate, (float(i[:-1]) for i in percent))}.items()

print(*(get_salary(name, rate, percent)))

