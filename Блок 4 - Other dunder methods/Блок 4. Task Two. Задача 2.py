class NewList:
    def __init__(self, initial_list):
        self.data = initial_list

    def __sub__(self, other):
        result = [item for item in self.data if item not in other.data]
        print(1)
        return result

    def __isub__(self, other):
        self.data = [item for item in self.data if item not in other.data]
        print(2)
        return self.data

    def get_list(self):
        return self.items


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2
print(res_1)  # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2
print(lst1)  # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True]
print(res_2)  # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2
print(res_3)  # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a
print(res_4)  # NewList: [1, 2]
lst = res_2.get_list()
print(lst)  # [1, 2, 3]