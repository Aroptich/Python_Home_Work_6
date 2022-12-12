nes (52 sloc)  3.14 KB

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).


def reading_files(path_file) -> list[str]:
    """Считываем содержимое файла и возвращаем список членов многочлена"""
    with open(path_file, 'r', encoding='UTF-8') as polynomial:
        a = polynomial.read().replace(' = 0', '')
        list_b = a.split('+')
    # Возвращаем список членов многочлена
    return list_b


def creating_coefficients(temp_list_of_coefficients: list[str]) -> list[str]:
    """Получаем список из членов многочлена и возвращаем список из коэффициентов"""
    list_of_coefficients = []
    for i in temp_list_of_coefficients:
        number = ''
        for _ in i:
            if _ == '*':
                break
            number += _
        list_of_coefficients.append(number)
    return list_of_coefficients


def sum_ccoefficients(*args) -> list[str]:
    """Выполняет сумму коэффициентов 2-ух многочленов"""
    a = list(map(sum, zip(list(map(int, args[0][0])), list(map(int, args[0][1])))))
    return list(map(str, a))


def creating_a_polynomial_layout(b, d) -> list[str]:
    """Получаем списоки из коэффициентов и членов многочлена. Возвращаем члены без коэффициентов"""
    diff_polynomial = []
    for j, k in zip(b, d):
        if j.startswith(k):
            diff_polynomial.append(j.replace(k, ''))

    return diff_polynomial
def recording_file(a):
    """Записываем получившийся результат сложения в новый файл"""
    with open('finally_file.txt', 'w', encoding='UTF-8') as finally_polynomial:
        finally_polynomial.writelines(f'{"+".join(a)} = 0')


# Создаем список из файлов
path_file = ['file1.txt', 'file2.txt']

# Создаем список для хранения данных из прочитаных файлов
temp_list = []
# Считываем и записываем в список файлы из директории
for i in path_file:
    temp_list.append(reading_files(i))
# print(temp_list)

# Создаем список для хранения списков из коэффициентов многочленов
list_of_coefficients = []
# Проходим по списку из многочленов и передаем каждый многочлен для отделения коэффициентов
for j in temp_list:
    list_of_coefficients.append(creating_coefficients(j))

v = [x + y for x, y in
     zip(sum_ccoefficients(list_of_coefficients), creating_a_polynomial_layout(temp_list[0], list_of_coefficients[0]))]
#Вызываем функцию, отвечающая за запись суммы двух многочленов
recording_file(v)
