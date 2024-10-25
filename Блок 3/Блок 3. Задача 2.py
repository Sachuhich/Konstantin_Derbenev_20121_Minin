'''
Задание 2. На вход подается 8-битное целое число со знаком (проверить нужно), на выходе вы должны вернуть перевернутое значение.
    Если значение выходит за пределы диапазона 8-битных целых чисел со знаком, тогда возвращаем сообщение ("пo solution").
    р.ѕ. Диапазон (-27,27-1)
Input: 12
Output: 21
Input: 123
Output: "no solution"
Input: -150
Output: -51
'''

num=int(input())
if num>=0:
    mun=int(str(num)[::-1])
    print(mun)if mun<128 else print('no solution')
else:
    num=str(num)[1::]
    mun=int((num)[::-1])
    print('-',mun,sep='')if mun<129 else print('no solution')
