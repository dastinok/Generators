'''Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.'''




file = "c:\\path\\sub_path\\file.png"

def get_path(path: str) -> tuple[str,str,str]:
    path_1, _, file = path.rpartition('\\')
    file, _, expansion = file.rpartition(".")
    return path_1, file, expansion


a = get_path(file)
print(a)