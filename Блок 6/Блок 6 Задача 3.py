'''
Задача 3: Вы санта. Вы попросили эльфа вернуть вам список пользователей, где каждый пользователь представляет собой еще один список,
    который содержит один или два элемента: строка (имя пользователя) и его почтовый индекс.
    Напишите функцию santa_users(), которая принимает двумерный список, и возвращает словарь с элементом для каждого пользователя,
    где ключ - это имя пользователя, а значение - почтовый индекс пользователя. Если нет индекса, тогда значение должно быть None.
Пример: [["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]. У одного пользователя есть имя, но нет индекса.
    santa_users() вернет этот словарь:
{
    "name1 surname1": 12345,
    "name2 surname2": None,
    "name3 surname3": 12354,
    "name4 surname4": 12435,    
}
'''

def santa_users(users_list):
    ans = {}
    for i in users_list:
        if len(i) == 2:
            name, code = i
            ans[name] = code
        else:
            name = i[0]
            ans[name] = None
    return ans

users_list = [
    ["name1 surname1", 12345],
    ["name2 surname2"],
    ["name3 surname3", 12354],
    ["name4 surname4", 12435]
]
for name, code in santa_users(users_list).items():
    print(f'{name}: {code}') # Выводим каждый элемент в отдельной строке
