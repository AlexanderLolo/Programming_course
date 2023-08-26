from functools import reduce


def army_communication_matrix(n: int, matrix: list) -> str:
    # Для каждой координаты находим матрицу с макиальной суммой, имеющую левый верхний угол в этой координате, и сравниваем друг с другом. 
    # Перебираем (n-1)^2 координат

    if n <= 2:
        return None

    summa = matrix[0][0] + sum_elem(0, 0, 2, matrix)
    x_val = 0
    y_val = 0
    size = 2

    for i in range(n-1):
        for j in range(n-1):
            mid_result = matrix_with_max_sum(i, j, n, matrix)
            if mid_result[0] > summa:
                summa = mid_result[0]
                x_val = i
                y_val = j
                size = mid_result[1]

    return str(x_val) + " " + str(y_val) + " " + str(size)


def sum_elem(x: int, y: int, size: int, matrix: list) -> int:
    # Суммируем элементы матрицы, которые стоят в x + size столбце с координатами y + size и в y + size строке с координатами x + size
    summa = reduce(lambda a, b: a + b, matrix[y + size - 1][x: x + size])
    for i in range(size - 1):
        summa += matrix[y + i][x + size - 1]

    return summa


def matrix_with_max_sum(x: int, y: int, n: int, matrix: list) -> list:
    # находим матрицу с максимальной суммой среди вложенных друг в друга матриц, с левым верхним улом в координате x,y
    # сложность не более O(n^2)
    summa = matrix[y][x] + sum_elem(x, y, 2, matrix)
    size = 2

    for i in range(3, min(n, n + 1 - max(x, y))):
        temp = summa + sum_elem(x, y, i, matrix)
        if temp > summa:
            summa = temp
            size = i

    return [summa, size]
