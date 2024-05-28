from random import *

matrix = [['+', '+', '+', '.', '+', '+'], ['+', '+', '+', '.', '.', '+'], ['+', '+', '+', '.', '+', '+'], ['+', '.', '.', '.', '.', '+'], ['.', '.', '.', '.', '.', '+'], ['+', '+', '+', '.', '+', '.']]
def make_matrix(n, m):
    return matrix


def starters(place, n, m):  # место старта
    start_x, start_y =  2,4
    place[start_x][start_y] = '#'
    return place, start_x, start_y

def search_path(matrix, start_x, start_y, n, m):
    next = [(start_x, start_y, 0)]
    visited = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while next:
        x, y, distance = next.pop(0)
        if (x, y) in visited:
            continue
        visited.append((x, y))

        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            if (x, y) != (start_x, start_y):
                return True, distance, (x + 1, y + 1)

        for move_x, move_y in directions:
            next_x, next_y = x + move_x, y + move_y
            if 0 <= next_x < n and 0 <= next_y < m and matrix[next_x][next_y] == '.' and (next_x, next_y) not in visited:
                next.append((next_x, next_y, distance + 1))

    return False, None, None

n, m = 6,6
place = make_matrix(n, m)
place, start_x, start_y = starters(place, n, m)

res = search_path(place, start_x, start_y, n, m)
print("Размер матрицы: ", n, "x", m)
print("Матрица:")
for i in range(n):
    for j in range(m):
        print(place[i][j], end=" ")
    print()
print("Старт:", (start_x + 1, start_y + 1))
print("Ответ:", res)