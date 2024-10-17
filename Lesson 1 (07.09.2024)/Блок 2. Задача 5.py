# Проверяет, что все цифры зад натрульного 3знач числа различны

num,d=int(input()),[]
if num>0 and len(str(num))==3:
    for i in range(len(str(num))):
        if str(num)[i]not in d:d.append(str(num)[i])
        else:
            print('В числе',num,'есть повторяющиеся цифры')
            exit()
    print('В числе',num,'нет повторяющихся цифр')
else:print('Число',num,'не натуральное или не трёхзначное')