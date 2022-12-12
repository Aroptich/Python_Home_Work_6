# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
import math
def list_of_prime_numbers() -> list[int]:
    N = int(input('Введите число: '))
    # Создаем список из целых чисел
    list_of_numbers = [i for i in range(2, N + 1)]
    list_a = []
    for x in list_of_numbers:
        # Вычисляем количество делителей числа
        div_number = math.floor(x ** 0.5)
        if div_number > 1:
            list_div_numbers = [x % y for y in range(2, round(x ** 0.5)+1)]
            if 0 not in list_div_numbers:
                list_a.append(x)
            # Очищаем список делителей
            list_div_numbers.clear()
        else:
            list_a.append(x)
    return list_a


print(list_of_prime_numbers())
