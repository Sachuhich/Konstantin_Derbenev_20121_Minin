'''
Задание 3. На вход поступает строка и целое значение.
    Необходимо вывести строку в зигзагообразном виде, где целое значение обозначает количество строк.
    Другими типами данных пользоваться нельзя. Начиная с верху вниз, как показано на рисунке.
Ввод: перфекционист, 3
Вывод: пеотефкинсрци
Ввод: перфекционист, 4
Вывод: пцтекисреоифн
Ввод: перфекционист, 1
Вывод: перфекционист
'''

string=input()
zig_input=string.split(', ')
word,colums,split_word=zig_input[0],int(zig_input[1]),[] # word - слово с Input, colums - количество строк
if colums>1:
    long=word
    while word:
        split_word.append(word[0:colums+colums-2]) # Записываюся символы по частям в зависимости от количества строк
        word=word[colums+colums-2:] # записанная часть убирается
    output,count='',0
    for i in range(len(split_word)):
        if len(split_word[i])<(2*colums-2):split_word[i]=split_word[i]+'*'*((2*colums-2)-len(split_word[i])) # Если в последней части меньше элементов, чем в остальных, то туда записываются '*'
    for z in range((len(split_word[0])//2)+1): # В этом цикле записывается в output ответ к задаче. Берутся первые элементы от каждой части, затем каждые первые и последние. И так до момента, пока элементы в split_word не кончатся
        for j in range(len(split_word)):
            if z==0:output+=split_word[j][z]
            elif z==(len(split_word[0])//2):output+=split_word[j][z]
            else:
                output+=split_word[j][z]
                output+=split_word[j][-z]
    output=output.replace('*','') # Убираются лишние '*'
    print(output)
elif colums==1:print(word)
else: print('Error: Zig zag is impossible') # В случае, если целое значение из Input меньше 1
