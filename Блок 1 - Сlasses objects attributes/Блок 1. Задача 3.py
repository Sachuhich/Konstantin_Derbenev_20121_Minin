'''
Объявите пустой класс с именем Car. С помощью функции setattr() добавьте в этот класс атрибуты:
model: "Тойота"
color: "Розовый"
number: "П111УУ77"
Выведите на экран значение атрибута color, используя словарь dict класса Car.
Если выведите на экран, то Print()
Подсказка: Словарь
'''

class Car:
    pass

setattr(Car,'model','Тойота')
setattr(Car,'color','Розовый')
setattr(Car,'number','П111УУ77')

print(Car.__dict__['color'])  # Вывод: Розовый