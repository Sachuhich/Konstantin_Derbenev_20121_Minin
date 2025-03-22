'''
Объявите класс с именем DataBase, который бы хранил в себе следующую информацию:
pk: 1
title: "Классы и объекты"
author: "Сергей Балакирев"
views: 14356
comments: 12
Имена переменных (атрибутов класса) используйте такие же (pk, title, author, views и comments) с соответствующими значениями.
'''

class DataBase:
    def __init__(self):
        self.pk= 1
        self.title='Классы и объекты'
        self.author='Сергей Балакирев'
        self.views=14356
        self.comments=12