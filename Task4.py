# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def multiplying_pairs_of_numbers_in_a_list(list_of_numbers: list) -> list:
    if type(list_of_numbers) in [list]:
        if len(list_of_numbers) % 2 == 1:
            list_a = [list_of_numbers[i] for i in range(len(list_of_numbers) // 2 + 1)]
            list_b = [list_of_numbers[i] for i in range(len(list_of_numbers) // 2, len(list_of_numbers))]
            return [x * y for x, y in zip(list_a, list_b[::-1])]
        list_a = [list_of_numbers[i] for i in range(len(list_of_numbers) // 2)]
        list_b = [list_of_numbers[i] for i in range(len(list_of_numbers) // 2, len(list_of_numbers))]
        return [x * y for x, y in zip(list_a, list_b[::-1])]
    return -1


print(multiplying_pairs_of_numbers_in_a_list([2, 3, 5, 6]))
