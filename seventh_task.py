'''✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку. '''

text = 'dfhvdsbfi'

dict_result = {i : ord(i) for i in text}
print(dict_result)

new_dict = iter(dict_result.items())
for _ in range(5):
    print(next(new_dict))