'''
Объявите класс с именем Notes и определите в нем следующие атрибуты:
uid: 1005435
title: "Шутка"
author: "И.С. Бах"
pages: 2
Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута author.
'''

class Notes:
    uid=1005435
    title='Шутка'
    author='И.С. Бах'
    pages=2

print(getattr(Notes,'author'))