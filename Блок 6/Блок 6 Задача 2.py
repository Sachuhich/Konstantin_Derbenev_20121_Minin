list0 = [1, 2, 3, 4]
list0 = ['a', 'b', 'c', 'd', 'd']

list0=list(set(list0)) # Удаление повторяющихся элементов
from itertools import combinations
d=[]
for i in range(1,len(list0)+1): # Генерация всех подмножеств
    for j in combinations(list0,i):
        sorted_j=tuple(sorted(j))
        d.append(sorted_j)
d=list(set(d)) # Удаление дубликатов
c=set()
for j in d: # Финальное множество
    j=str(j).replace(',','')
    j=str(j).replace('(','',)
    j=str(j).replace(')','',)
    j=str(j).replace(' ','',)
    c.add(j)
c=sorted(c,key=lambda x:(len(x),x)) # Сортировать по значению и длине
print('Подмножества:',c,'\nКоличество подмножеств:',len(sorted(c)))