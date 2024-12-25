def read_input(file_path):
    with open(file_path, 'r') as f:
        N, L, K = map(int, f.readline().strip().split())
        positions = [tuple(map(int, f.readline().strip().split())) for _ in range(K)]
    return N, L, K, positions

def is_under_threat(board, x, y, N):
    # Проверяем угрозы слона (через 2 клетки по диагонали)
    directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == '#':
            return True
    return False

def place_figures(board, placed, positions, target_count, N, solutions):
    if placed == target_count:
        solutions.append(positions[:])
        return

    for x in range(N):
        for y in range(N):
            if board[x][y] == '0' and not is_under_threat(board, x, y, N):
                # Помечаем фигуру на доске
                board[x][y] = '#'
                positions.append((x, y))

                # Рекурсивно размещаем следующие фигуры
                place_figures(board, placed + 1, positions, target_count, N, solutions)

                # Убираем фигуру (откат)
                board[x][y] = '0'
                positions.pop()

def print_board_to_console(board):
    for row in board:
        print(" ".join(row))

def write_output(file_path, solutions):
    with open(file_path, 'w') as f:
        if not solutions:
            f.write("no solutions\n")
        else:
            for pos in solutions:
                f.write(", ".join(f"({x},{y})" for x, y in pos) + "\n")

# Чтение входных данных
N, L, K, initial_positions = read_input('input.txt')

# Инициализация доски
board = [['0' for _ in range(N)] for _ in range(N)]

# Установка уже существующих фигур
for x, y in initial_positions:
    board[x][y] = '#'

# Вычисляем угрозы от существующих фигур
for x, y in initial_positions:
    is_under_threat(board, x, y, N)

# Хранение решений
solutions = []

# Размещение новых фигур
place_figures(board, 0, [], L, N, solutions)

# Запись вывода в файл
write_output('output.txt', solutions)

# Печать текущего состояния доски
print_board_to_console(board)