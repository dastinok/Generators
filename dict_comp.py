dict_comp = {i: chr(i) for i in range(97, 123)}
print(dict_comp)
for number, char in dict_comp.items():
    print(f'dict[{number}] = {char}')