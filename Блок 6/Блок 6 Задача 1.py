'''
Задача 1: Функция получает два списка. В каждом списке не должно быть дубликатов.
Функция возвращает:
    1) Количество элементов, присутствующих в обоих списках
    2) Количество элементов, присутствующих только в одном списке
    3) Количество оставшихся элементов в list1 после извлечения элементов из list2
    4) Количество оставшихся элементов в list2 после извлечения элементов из list1
Пример:
    list1, list2 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
    1) 3 элемента: 16, 25, 47
    2) 19 элементов: 0, 1, 6, 7, 8, 10, 12, 13, 18, 20, 22, 23, 33, 37, 38, 40, 41, 44, 48
    3) 9 элементов: 0, 33, 37, 6, 10, 44, 13, 18, 22
    4) 10 элементов: 1, 38, 7, 8, 41, 40, 12, 48, 20, 23
'''

def funcName(list1, list2):
    ans1=[set(list1).intersection(set(list2)),len(set(list1).intersection(set(list2)))]
    ans2=[set(list1).symmetric_difference(set(list2)),len(set(list1).symmetric_difference(set(list2)))]
    ans3=[set(list1).difference(set(list2)),len(set(list1).difference(set(list2)))]
    ans4=[set(list2).difference(set(list1)),len(set(list2).difference(set(list1)))]
    return(ans1,ans2,ans3,ans4)

if __name__ == "__main__":
    c,list1,list2=1,input(),input() #[0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
    for i in funcName(list1, list2):
        print(str(c)+')',i[1],'элемента:',i[0])
        c+=1
