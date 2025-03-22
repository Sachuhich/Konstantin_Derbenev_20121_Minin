'''
Из входного потока читаются строки данных с помощью команды:
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
в формате: id, name, old, salary (записанные через пробел). Например:
1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
…
То есть, каждая строка - это элемент списка lst_in.
Необходимо в класс DataBase:

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

добавить два метода:
select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне [a; b] (включительно) по их индексам (не id, а индексам списка);
также учесть, что граница b может превышать длину списка.
insert(self, data) - для добавления в список lst_data новых данных из переданного списка строк data;
Каждая запись в списке lst_data должна быть представлена словарем в формате:
{‘id’: ‘номер’, ‘name’: ‘имя’, ‘old’: ‘возраст’, ‘salary’: ‘зарплата’}
Например:
{‘id’: ‘1’, ‘name’: ‘Сергей’, ‘old’: ‘35’, ‘salary’: ‘120000’}
Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей в коллекции FIELDS.
P. S. Ваша задача только добавить два метода в класс DataBase.

Sample Input:
1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
Useful func: zip()
import sys
# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
# Or use this definition instead stream:
# lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000','3 Иван 13 1200']
class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
    # здесь добавлять методы
db = DataBase()
db.insert(lst_in)
'''

import sys

#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000','3 Иван 13 1200']

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self,data):
        for line in data:
            values=line.split()
            record=dict(zip(self.FIELDS,values))
            self.lst_data.append(record)

    def select(self,a,b):
        return self.lst_data[a:b+1]

db = DataBase()
db.insert(lst_in)
print(db.select(0, 1))