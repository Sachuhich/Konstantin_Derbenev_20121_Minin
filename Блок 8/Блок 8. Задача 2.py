def has_exit(maze):
    c,d=0,0
    for i in range(len(maze)):  # Находим координаты Кейт
        for j in range(len(maze[i])):
            if maze[i][j] == 'k':
                c+=1
                stack = [(i, j)]  # Начинаем с позиции Кейт
            # if maze[i][j]=='#'or' ':

    if c>1: raise Exception('Кейт должна быть одна')
    if c==len(maze): return True # Если лабиринта не существует
    if c==0: raise Exception('В лабиринте нету Кейт')

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Возможные шаги: вниз, вверх, вправо, влево
    visited = set()  # Задаётся именно set(), что бы Кейт не шагала в обратную сторону.

    while stack:
        x, y = stack.pop()  # Извлекает последнюю добавленную координату

        if (x == 0 or y == 0 or x == len(maze) - 1 or y == len(maze[x]) - 1) and maze[x][y] == ' ': # Проверка на границу лабиринта и пустую клетку (если выход найден)
            return True  # Выход найден

        visited.add((x, y))  # Добавляем текущие координаты в посещенные

        for dx, dy in directions:  # Проверяем возможность движения в разных направлениях
            new_x, new_y = x + dx, y + dy  # Вычисляем новые координаты
            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[new_x]) and (new_x, new_y) not in visited): # Если координаты в пределах лабиринта и клетка не была посещена
                if maze[new_x][new_y] == ' ':  # Если клетка свободна (не стена)
                    stack.append((new_x, new_y))  # Добавляем новое местоположение в стек
    return False  # Если выход не найден

maze = ["########",
        "  # ## #",
        "# #k#  #",
        "# # # ##",
        "# # #  #",
        "#     ##",
        "########"]
print(has_exit(maze))