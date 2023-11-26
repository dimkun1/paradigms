from datetime import datetime

# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers: list):
    count = 0
    for _ in numbers:
        count += 1
    for i in range(count):
        for j in range(i, count):
            if numbers[i] < numbers[j]:
                temp = numbers[j]
                numbers[j] = numbers[i]
                numbers[i] = temp
    return numbers

# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers: list):
    return sorted(numbers, reverse=True)


if __name__ == "__main__":
    num = [9, -8, 5, 2, 6, 9, 20, 1111]
    print(num)

    print(sort_list_imperative(num))

    # print(sort_list_declarative(num))