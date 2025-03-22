'''
Выберите верное значение атрибута, которое будет выведено на экран при выполнении следующей программы:
class Figures:
    type = 'ellipse'
    color = 'red'
fig1 = Figures()
print(fig1.color)
Выдаст ошибку, т.к. свойства color нет в объекте fig1
False
red
None
'''

class Figures:
    type = 'ellipse'
    color = 'red'
fig1 = Figures()
print(fig1.color)
