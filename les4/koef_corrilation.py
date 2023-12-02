from math import sqrt, pow


def corrilation(data_1: list[float], data_2: list[float]) -> float:
    avg_1 = sum(data_1) / len(data_1)
    avg_2 = sum(data_2) / len(data_2)

    return sum(map(lambda x, y: (x - avg_1) * (y - avg_2), data_1, data_2)) / \
           (sqrt(sum(map(lambda x: pow(x - avg_1, 2), data_1))) * sqrt(sum(map(lambda y: pow(y - avg_2, 2), data_2))))


print(corrilation([60, 65, 72, 70, 74, 63, 66, 68, 67, 69, 70, 64],\
                  [120, 140, 180, 184, 190, 160, 155, 158, 170, 190, 210, 150]))