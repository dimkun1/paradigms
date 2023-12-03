def binary_find(lst: list, num: int) -> int:
    low_limit = 0
    high_limit = len(lst) - 1
    find_index = high_limit // 2
    while find_index <= high_limit and find_index >= low_limit:
        if lst[find_index] == num:
            return find_index
        if lst[find_index] < num:
            low_limit = find_index + 1
        elif lst[find_index] > num:
            high_limit = find_index - 1
        find_index = (high_limit + low_limit) // 2
    return -1


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(14):
        print(f'{i} - {binary_find(lst, i)}')