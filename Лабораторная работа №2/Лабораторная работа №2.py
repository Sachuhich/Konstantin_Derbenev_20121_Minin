def safe(board,row,col,N): # Проверяет, находится ли клетка под боем другой фигуры
    for i in range(-2,3): # Клетки под боем находим в промежутке от -2 до +2, остальную доску брать в расчёт смысла нет
        for j in range(-2,3):
            if abs(i)==abs(j) and (i!=0 or j!=0): # Проверяем только диагональные клетки
                r,c=row+i,col+j # Координаты клетки под боем
                if 0<=r<N and 0<=c<N and board[r][c]==1: return False  # Если клетка под боем
    return True # Если клетка безопасна

def place_figures(board,figures,placed,L,N): # Размещаем фигуры на доске
    if placed==L: return [figures.copy()] # Если все нужные фигуры размещены, возвращаем копию текущего расположения фигур
    solutions=[] # Список для хранения возможных решений
    for i in range(N): # Строки
        for j in range(N): # Столбцы
            if board[i][j]==0 and safe(board,i,j,N): # Проверка безопасности клетки
                board[i][j]=1 # Устанавливаем фигуру
                figures.append((i,j)) # Добавляем координаты в список
                solutions.extend(place_figures(board,figures,placed+1,L,N)) # Рекурсивно размещаем следующую фигуру
                figures.pop() # Убираем последнюю добавленную фигуру
                board[i][j]=0 # Убираем фигуру с клетки
    return solutions # Все найденные решения

def print_board(board,N): # Выводит доску в консоль
    print('Изначальная доска:')
    for i in range(N): # Строки
        for j in range(N): # Столбцы
            if board[i][j]==1: print('#',end=' ') # Если клетка занята
            elif board[i][j] == 2: print('*',end=' ') # Если клетка под боем
            else: print('0',end=' ') # Если клетка пуста
        print() # Переход на новую строку

with open('input.txt','r') as file:
    N,L,K=map(int,file.readline().strip().split())
    board=[[0]*N for _ in range(N)] # Создаем доску
    current_figures=[] # Список координат размещенных фигур
    for _ in range(K): # Непоставленные фигуры
        x,y=map(int,file.readline().strip().split())
        board[x][y]=1 # Отмечаем, что клетка занята
        current_figures.append((x,y))

    for (x,y) in current_figures: # Перебираем фигуры, идентифицируя клетки под боем
        for i in range(-2,3): # Промежуток нахождения клеток под боем
            for j in range(-2,3):
                if abs(i)==abs(j) and (i!=0 or j!=0): # Проверяем только диагональные клетки
                    r,c=x+i,y+j # Координаты клетки под боем
                    if 0<=r<N and 0<=c<N: board[r][c]=2 # Метим клетку под боем

    solutions=place_figures(board,current_figures,0,L,N) # Функция для размещения фигур
    c=0 # Счётчик количества решений
    with open('output.txt','w') as out_file:
        if not solutions: out_file.write('no solutions\n') # Если решений нет
        else:
            for solution in solutions: # Перебираем все найденные решения
                formatted_solution = ', '.join(f'({x},{y})' for (x,y) in solution)  # Форматируем решение
                c+=1
                out_file.write(f'{formatted_solution}\n')  # Записываем решение в файл

    print_board(board, N) # Выводим доску в консоль
    print('Всего решений:',c//(K+L))
