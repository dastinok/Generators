names = ['Валерий', 'Артур', 'Андрей', 'Василий']
salary = [15000, 20000, 18000, 50000]
bonus = ['10.25%', '15.00%', '18.50%', '12.05%']


def salary_gen(names: list[str], salary: list[int], bonus: list[str]) -> dict[str: float]:
    return {name: sale / 100 * bon for name, sale, bon in zip(names, salary, (float(i[:-1]) for i in bonus))}.items()


print(*(salary_gen(names, salary, bonus)))
