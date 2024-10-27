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