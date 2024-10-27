matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
if not matrix: print([])  # Если матрица пуста
else:
    result,top,bottom,left,right = [],0,len(matrix)-1,0,len(matrix[0])-1 # Список, указание границ

    while top<=bottom and left<=right: # Цикл, продолжающийся пока границы не пересеклись
        result += matrix[top][left:right+1] # Движение вправо
        top+=1 # Движение вниз
        result += [matrix[i][right] for i in range(top,bottom+1)] # Движение вниз
        right-=1# Движение влево

        if top<=bottom: # Проверка, есть ли строки для добавления
            result += matrix[bottom][left:right + 1][::-1]  # Добавляем нижнюю строку в обратном порядке
            bottom-=1  # Сдвигаем нижнюю границу вверх

        if left<=right: # Проверка, остался ли хотя бы один столбец для добавления (движение вверх)
            result += [matrix[i][left] for i in range(bottom,top-1,-1)]  # Добавляем левый столбец в обратном порядке
            left+=1  # Сдвигаем левую границу вправо
    print(result)