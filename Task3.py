# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
def sum_of_elements_at_odd_indices(list_of_numbers: list) -> int:
    if type(list_of_numbers) in [list]:
        return sum([i for i in list_of_numbers[1::2]])
    return -1

print(sum_of_elements_at_odd_indices([2, 3, 5, 9, 3]))
