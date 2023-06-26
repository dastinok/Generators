# Таблица умножения в виде однострочного генератора


def mult_table(size):
    for i in range(1,11):
        for j in range(1, size // 2 + 1):
            print(f'{j} x {i} = {i * j}', end=' ' * (15 - len(f'{j} x {i} = {i * j}')))

        print()
    print()
    for i in range(1, 11):
        for j in range(size // 2 + 1, size + 1):
            print(f'{j} x {i} = {i * j}', end=' ' * (15 - len(f'{j} x {i} = {i * j}')))
        print()

print(*((f'{x} * {y} = {x*y}   {x+5} * {y} = {(x+5)*y} ') for x in range(1,6) for y in range(1,11) ), sep='\n')


mult_table(10)

