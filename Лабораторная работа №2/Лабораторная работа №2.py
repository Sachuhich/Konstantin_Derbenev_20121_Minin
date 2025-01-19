def print_board(N, board): # Функция для отображения доски. Чтобы Доска отобразилась в консоли, впишите до "__main__" - "print_board(N,board)"
    for i in range(N):
        row=''
        for j in range(N):
            if board[i][j]==1: row+='# '
            elif board[i][j]==2: row+='* '
            else: row+='0 '
        print(row.strip())

def mark_attacks(N, board, x, y): # Функция для пометки клеток, которые атакует фигура. Атакует только две ближайшие диагональные клетки.
    directions = [(-1,-1),(-1,1),(1,-1),(1,1)] # Направления для фигуры (диагонали)
    for dx, dy in directions: # Для каждой диагонали проверяем две ближайшие клетки
        # Первая клетка
        nx, ny = x + dx, y + dy
        if 0<=nx<N and 0<=ny<N: board[nx][ny]=2 # Помечаем как атакуемую клетку
        # Вторая клетка
        nx, ny = x + 2 * dx, y + 2 * dy
        if 0<=nx<N and 0<=ny<N: board[nx][ny]=2 # Помечаем как атакуемую клетку

def main():
    with open('input.txt', 'r') as f: # Чтение входных данных из файла
        N,L,K = map(int,f.readline().split())
        already_placed = [tuple(map(int, f.readline().split())) for _ in range(K)] # Позиции уже стоящих фигур

    board = [[0] * N for _ in range(N)]  # Инициализация доски
    for x,y in already_placed: board[x][y]=1  # Ставим фигуру на доску
    for x,y in already_placed: mark_attacks(N,board,x,y) # Для каждой фигуры на доске помечаем её ходы

    with open('output.txt', 'w') as f: # Запись в файл в формате "x y"
        if already_placed:
            solution_str = '\n'.join(f'{x} {y}' for x,y in already_placed)
            f.write(solution_str+'\n')
        else: f.write("no solutions\n")

if __name__ == "__main__":
    main()
