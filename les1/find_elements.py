# Контекст
# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
# ли target в array. Такую процедуру будем называть поиском.

# Задача
# Реализовать императивную функцию поиска элементов на языке Python.



def find_elements(input_list: list, target: int) -> bool:
    for i in input_list:
        if target == i:
            return True
    return False

if __name__ == "__main__":
    print(find_elements([1, 2, 3, 4, 5], 8))

# Задача
# Реализовать декларативную функцию поиска элементов на языке Python.

def find_elements(input_list: list, target: int) -> bool:
    return target in input_list