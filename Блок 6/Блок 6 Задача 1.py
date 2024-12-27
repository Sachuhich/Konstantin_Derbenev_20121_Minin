'''
Задача 1: Функция получает два списка. В каждом списке не должно быть дубликатов.
Функция возвращает:
    1) Количество элементов, присутствующих в обоих списках
    2) Количество элементов, присутствующих только в одном списке
    3) Количество оставшихся элементов в list1 после извлечения элементов из list2
    4) Количество оставшихся элементов в list2 после извлечения элементов из list1
Пример:
    list1= 0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25
    list2= 1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25
    1) 3 элемента: 16, 25, 47
    2) 19 элементов: 0, 1, 6, 7, 8, 10, 12, 13, 18, 20, 22, 23, 33, 37, 38, 40, 41, 44, 48
    3) 9 элементов: 0, 33, 37, 6, 10, 44, 13, 18, 22
    4) 10 элементов: 1, 38, 7, 8, 41, 40, 12, 48, 20, 23
'''

def funcName(list1,list2):

    # 1) Элементы, присутствующие в обоих списках:
    com=set(list1).intersection(set(list2))
    c_com=len(set(list1).intersection(set(list2)))

    # 2) Элементы, присутствующие только в одном списке:
    unique=set(list1).symmetric_difference(set(list2))
    c_unique=len(unique)

    # 3) Оставшиеся элементы в list1 после извлечения элементов из list2:
    remaining_1=set(list1).difference(set(list2))
    c_remaining_1=len(remaining_1)

    # 4) Оставшиеся элементы в list2 после извлечения элементов из list1:
    remaining_2=set(list2).difference(set(list1))
    c_remaining_2=len(remaining_2)

    return (com,c_com,unique,c_unique,remaining_1,c_remaining_1,remaining_2,c_remaining_2)

if __name__ == "__main__":
    list1 = list(map(int,input('').split(','))) # 0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25
    list2 = list(map(int,input('').split(','))) # 1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25
    results = funcName(list1,list2)
    print("1)",results[1],"элементов:",results[0])
    print("2)",results[3],"элементов:",results[2])
    print("3)",results[5],"элементов:",results[4])
    print("4)",results[7],"элементов:",results[6])
