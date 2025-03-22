'''
Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:

add(self, eng, rus) - для добавления новой связки английского и русского слова (если английское слово уже существует,
                то новое русское слово добавляется как синоним для перевода, например, go - идти, ходить, ехать);
                если связка eng-rus уже существует, то второй раз ее добавлять не нужно, например: add(‘go’, ‘идти’), add(‘go’, ‘идти’);
remove(self, eng) - для удаления связки по указанному английскому слову;
translate(self, eng) - для перевода с английского на русский
                (метод должен возвращать список из русских слов, соответствующих переводу английского слова, даже если в списке всего одно слово).

Все добавления и удаления связок должны выполняться внутри каждого конкретного объекта класса Translator,
                т.е. связки хранить локально внутри экземпляров классов класса Translator.
Создайте экземпляр tr класса Translator и вызовите метод add для следующих связок:
                tree - дерево
                car - машина
                car - автомобиль
                leaf - лист
                river - река
                go - идти
                go - ехать
                go - ходить
                milk - молоко
Затем методом remove() удалите связку для английского слова car. С помощью метода translate() переведите слово go.
                Результат выведите на экран в виде строки из всех русских слов, связанных со словом go:
Вывод в формате: идти ехать ходить
'''

class Translator:
    def __init__(self):
        self.words={}

    def add(self,eng,rus):
        if eng not in self.words:
            self.words[eng]=[]
        if rus not in self.words[eng]:
            self.words[eng].append(rus)

    def remove(self,eng):
        if eng in self.words:
            del self.words[eng]

    def translate(self,eng):
        return self.words.get(eng,[])

tr = Translator()

tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')
translation = tr.translate('go')
print(' '.join(translation))