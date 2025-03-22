class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title=title
        self.author=author
        self.pages=pages
        self.year=year

    def __setattr__(self, key, value):
        if key in ['title', 'author'] and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных. Ожидается строка.")
        elif key in ['pages', 'year'] and not isinstance(value, int):
            raise TypeError("Неверный тип присваиваемых данных. Ожидается целое число.")

        object.__setattr__(self, key, value)

    def __str__(self):
        return (f'Заголовок: {self.title}, Автор: {self.author}, Число страниц: {self.pages}, Год издания: {self.year}')

book=Book('OOP','JK',23,2022)
print(book)