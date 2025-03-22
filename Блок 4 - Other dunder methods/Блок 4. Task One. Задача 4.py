'''
Объявите класс WordString, объекты которого создаются командами:

w1 = WordString()
w2 = WordString(string)

где string - передаваемая строка. Например:

words = WordString("Python ООП")

Реализовать следующий функционал для объектов этого класса:
len(words) - должно возвращаться число слов в переданной строке (слова разделяются
одним или несколькими пробелами);
words(indx) - должно возвращаться слово по его индексу (indx - порядковый номер слова в
строке, начиная с 0).
Также в классе WordString реализовать объект-свойство (property):
string - для передачи и считывания строки.
Пример пользования классом WordString (эти строчки в программе писать не нужно):

words = WordString()
words.string = "Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
'''

class WordString:
    def __init__(self, string=''):
        self.string=string

    def __len__(self):
        return len([word for word in self.string.split() if word])

class WordString:
    def __init__(self, string=''):
        self._string = string

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value

    def __len__(self):
        return len(self._string.split())

    def __call__(self, indx):
        words = self._string.split()
        if 0 <= indx < len(words):
            return words[indx]
        return ''

words = WordString()
words.string = 'Python ООП'
n = len(words)
first = '' if n == 0 else words(0)
print(words.string)
print(f'Число слов: {n}; первое слово: {first}')