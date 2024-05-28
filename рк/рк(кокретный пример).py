import random

matrix = [['+', '+', '+', '.', '+', '+'], ['+', '+', '+', '.', '.', '+'], ['+', '+', '+', '.', '+', '+'], ['+', '.', '.', '.', '.', '+']
          , ['+', '.', '.', '.', '.', '.'], ['+', '+', '+', '.', '+', '.']]
def create_matrix(N, M):  # создание матрицы
    return matrix


def matrix_destroy(matrix, N, M):  # для прохождения матрицы
    start_x, start_y = 2, 4
    matrix[start_x][start_y] = '#'
    return matrix, (start_x, start_y)


def find_path(place, start):  # ищем путь к звездам(выходу)
    qu = [(start_x, start_y, 0)]
    visited = ()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # куда можем двигаться(вверх, вниз, вправо, влево)

    while qu:
        x, y, dist = qu.pop(0)  # извлекаем координаты, удаляя их из массива
        if (x, y) in visited:  # если клетки уже посещены, то их не рассматриваем их
            continue
        visited.add((x, y))  # координаты уже посещенных клеток

        if x == 0 or x == N - 1 or y == 0 or y == M - 1:  # если с краю
            if (x, y) != (start_x, start_y):
                return True, dist, (x+1, y+1)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and place[nx][ny] == '.' and (nx, ny) not in visited: #  проверка
                qu.append((nx, ny, dist + 1)) # записываем в список координаты пути

    return False, None, None


def hide_exit(place):
    N, M = len(place), len(place[0])
    exits = []
    for x in range(N):
        if place[x][0] == '.':
            exits.append((x, 0))
        if place[x][M - 1] == '.':
            exits.append((x, M - 1))
    for y in range(M):
        if place[0][y] == '.':
            exits.append((0, y))
        if place[N - 1][y] == '.':
            exits.append((N - 1, y))
    return exits


N, M = 6, 6
place = create_matrix(N, M)
place, start = matrix_destroy(place)

exits = hide_exit(place)

res = find_path(place, start)
print("Матрица:")
for row in place:
    print(' '.join(row))
print("\nПуть:", exits)
print("Начало:", start)
print("Результат, координаты выхода:", res)
