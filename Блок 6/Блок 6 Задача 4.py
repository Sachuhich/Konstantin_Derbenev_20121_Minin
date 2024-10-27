'''
Задача 4: Реализуйте функцию, принимающую один аргумент (римское число) и возвращающее арабское.
'''

def func(str):
    num={'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    result,before=0,0
    for i in reversed(str):
        now=num[i]
        if now<before: result-=now # Если текущее значение меньше предыдущего, то вычитаем
        else: result+=now # Если текущее значение больше предыдущего, то прибавляем
        before=now
    return result

ans=str(input().upper()) # "LVI"
print(func(ans))
