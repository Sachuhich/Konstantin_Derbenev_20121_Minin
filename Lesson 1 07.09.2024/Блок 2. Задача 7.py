# Даны 3 целых числа. Определить, сколько среди них совпадают. Вывод: ВСЕ СОВПАДАЮТ, 2 СОВП, НИКАКОЕ НЕ СОВПАДАЕТ

list,c=[int(input()),int(input()),int(input())],0
list.sort()
for i in range(len(list)-1):
    if list[i]==list[i+1]:c+=1
if c==2:print('Все числа совпадают')
elif c==1:print('Два числа совпадают')
else:print('Никакие из чисел не совпадают')