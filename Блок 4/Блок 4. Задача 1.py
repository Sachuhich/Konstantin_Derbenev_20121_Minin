'''
Задача 1. С клавиатуры поступает строка.
  Необходимо вывести самую длинную подстроку без повторных символов.
Input: “qweasdfdqw"
Output: "qweasd"
Input: "aaaaaaa"
Output: "a"
Input: "prrker"
Output: "rke"
'''

a = str(input())
used,s,lst,end= '','',[],''
for i in range(len(a)):
  if a[i] not in used: # Выделяется подстрока
      used+=a[i]
      s+=a[i]
  else: # Добавление выделеной подстроки в lst, начало выделения новой подстроки
      lst.append([s, len(s)])
      s,used=a[i],a[i]
if len(lst)>1: # Если подстрок несколько, ищем самую длинную
  for i in range(len(lst)-1):
    if lst[i][1]>lst[i+1][1]:
      end=lst[i][0]
    else:
      end=lst[i+1][0]
  print(end)
else:print(lst[0][0])
