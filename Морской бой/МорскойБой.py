from random import randint


class Ship:
    # Конструктор класса Ship - инициализирует объект корабля
    def __init__(self, length, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp               # 1- 2|
        self._is_move = True        # Флаг движения
        self._cells = [1]*length  # 1 целая, 2 поврежденная

    def set_start_coords(self,x,y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return (self._x,self._y)

    def move(self, go):
        if not self._is_move:return False   # подбили

        if self._tp == 1:self._x += go
        else:self._y += go
        return True

    # Метод для проверки столкновения с другим кораблем
    def is_collide(self, ship):
        self_cells = self.get_all_cells()   # текущ корабля
        other_cells = ship.get_all_cells()  # друго корабля

        for x1,y1 in self_cells:
            for x2,y2 in other_cells:
                if abs(x1-x2)<=1 and abs(y1-y2)<=1:return True #столкнулись

        return False #нет столкновения

    def is_out_pole(self, size):
        cells = self.get_all_cells()                            # все клетки, занимаемые кораблем
        for x, y in cells:
            if x<0 or x>=size or y<0 or y>=size:return True     # клетка за границей

        return False

    def get_all_cells(self):
        cells = []
        for i in range(self._length):
            if self._tp==1:cells.append((self._x+i,self._y))  # -
            else:cells.append((self._x,self._y+i)) # |
        return cells

    def __getitem__(self,index):
        return self._cells[index]
    def __setitem__(self,index,value):
        self._cells[index]=value
        if value==2:self._is_move=False     #попали=не двигаемся


class GamePole:
    def __init__(self,size):
        self._size=size
        self._ships=[]

    def init(self):
        self._ships = []
        self._ships.append(Ship(4,tp=randint(1,2)))
        for _ in range(2):self._ships.append(Ship(3,tp=randint(1,2)))
        for _ in range(3):self._ships.append(Ship(2,tp=randint(1,2)))
        for _ in range(4):self._ships.append(Ship(1,tp=randint(1,2)))
        self._place_ships()

    def _place_ships(self):
        ships_sorted=sorted(self._ships,key=lambda x:x._length,reverse=True)   #от большего к меньшему

        for ship in ships_sorted:
            placed = False
            attempts = 0                                     # Счетчик попыток размещения
            while not placed and attempts<1000:              # ограничение на попытки
                attempts+=1

                if ship._tp==1:  # -
                    x=randint(0,self._size-ship._length)
                    y=randint(0,self._size-1)
                else:            # |
                    x=randint(0,self._size-1)
                    y=randint(0,self._size-ship._length)

                ship.set_start_coords(x,y)   # корды кораблей

                if not ship.is_out_pole(self._size): # Проверяем валидность позиции
                    collision=False                  # столкновение
                    for other_ship in self._ships:   # с другими кораблями
                        # Пропускаем текущий корабль и корабли без координат
                        if other_ship!=ship and other_ship.get_start_coords()!=(None,None):
                            if ship.is_collide(other_ship):
                                collision = True
                                break

                    if not collision:placed=True # Если столкновений нет, корабль размещен
                else:
                    # Если корабль выходит за пределы, пробуем сменить ориентацию
                    # Меняем 1 на 2 и наоборот (3-1=2, 3-2=1)
                    ship._tp=3-ship._tp

                    # Пересчитываем координаты для новой ориентации
                    if ship._tp==1:  # -
                        x=randint(0,self._size-ship._length)
                        y=randint(0,self._size-1)
                    else:            # |
                        x=randint(0,self._size-1)
                        y=randint(0,self._size-ship._length)

                    # Устанавливаем новые координаты
                    ship.set_start_coords(x, y)

                    # Снова проверяем валидность позиции
                    if not ship.is_out_pole(self._size):
                        collision=False
                        for other_ship in self._ships:
                            if other_ship!=ship and other_ship.get_start_coords()!=(None,None):
                                if ship.is_collide(other_ship):
                                    collision=True      # есть столкновение
                                    break

                        placed=True    # без столкновений

    def get_ships(self):
        return self._ships  # список кораблей

    # для перемещения всех кораблей, которые могут двигаться
    def move_ships(self):
        for ship in self._ships:
            if not ship._is_move:continue               # Пропускаем корабли, которые не могут двигаться
            go=randint(0,1)*2-1                   # рандомно перемещаем
            original_x,original_y = ship._x,ship._y     # на случай отката
            ship.move(go)

            valid=True                                  # валидность новой позиции
            if ship.is_out_pole(self._size):valid=False #не столкнулись
            else:
                for other_ship in self._ships:
                    if other_ship!=ship and ship.is_collide(other_ship):
                        valid=False
                        break

            if not valid:                               # невалидна
                ship.set_start_coords(original_x, original_y)
                go = -go                                # в противоположном направлении
                ship.move(go)

                valid=True
                if ship.is_out_pole(self._size):valid=False
                else:
                    for other_ship in self._ships:
                        if other_ship!=ship and ship.is_collide(other_ship):
                            valid=False
                            break

                if not valid: # если до сих пор невалидна
                   ship.set_start_coords(original_x,original_y)


    def show(self):                   # отображение в консоли
        field = [[0 for _ in range(self._size)]for _ in range(self._size)]

        for ship in self._ships:      # корабли
            cells=ship.get_all_cells()
            for i,(x,y) in enumerate(cells):
                if 0<=x<self._size and 0<=y<self._size:    # корды в пределах поля
                    field[y][x]=ship[i]

        for row in field:
            print(' '.join(map(str,row)))

    def get_pole(self):              # метод для получения текущего состояния игрового поля
        field = [[0 for _ in range(self._size)]for _ in range(self._size)]

        for ship in self._ships:
            cells = ship.get_all_cells()
            for i,(x,y) in enumerate(cells):
                if 0<=x<self._size and 0<=y<self._size:
                    field[y][x]=ship[i]

        return tuple(tuple(row) for row in field)   # Преобразуем в кортеж кортежей



if __name__ == "__main__":
    SIZE_GAME_POLE = 7

    pole = GamePole(SIZE_GAME_POLE)
    pole.init()
    pole.show()
    print()
    pole.move_ships()
    pole.show()

# Tests
ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)
assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"
ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"
ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(
    s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"
s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"
s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"
s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"
s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"
p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"
        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"
pole_size_8 = GamePole(8)
pole_size_8.init()
print("\n Passed")