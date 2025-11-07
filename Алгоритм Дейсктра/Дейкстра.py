from typing import List, Tuple, Dict, Optional, Any
import heapq


class Vertex:
    """    Класс для представления вершин графа    """
    def __init__(self)->None:
        self._links:List['Link']=[]    # для хранения связей этой вершины

    @property
    def links(self)->List['Link']: return self._links    # Свойство для получения списка связей вершины

    def __lt__(self,other:Any)->bool:
        return id(self)<id(other)      # Сравниваем вершины по их id для работы в приоритетной очереди


class Link:
    """    Класс для описания связи между двумя вершинами графа    """
    def __init__(self,v1:Vertex,v2:Vertex,dist:int=1)->None:
        self._v1=v1
        self._v2=v2
        self._dist=dist

    @property
    def v1(self)->Vertex: return self._v1
    @property
    def v2(self)->Vertex: return self._v2
    @property
    def dist(self)->int: return self._dist
    @dist.setter
    def dist(self,value:int)->None: self._dist=value

    def get_other_vertex(self,vertex:Vertex)->Vertex:
        if vertex == self._v1: return self._v2  # переданная вершина=1 -> возвращаем 2
        else: return self._v1                   # переданная вершина=2 -> возвращаем 1

    def __eq__(self,other:Any)->bool:
        """    Проверка равенства связей по вершинам (независимо от порядка)    """
        if not isinstance(other,Link): return False
        # Две связи считаются равными, если они соединяют одинаковые вершины
        return (self.v1 == other.v1 and self.v2 == other.v2) or (self.v1 == other.v2 and self.v2 == other.v1)


class LinkedGraph:
    """    Класс для представления связного графа    """
    def __init__(self) -> None:
        self._links: List[Link]=[]    # для всех связей графа
        self._vertex: List[Vertex]=[] # для всех вершин графа

    def add_vertex(self, v: Vertex) -> None:
        # есть ли вершина в списке вершин графа
        if v not in self._vertex: self._vertex.append(v)

    def add_link(self, link: Link) -> None:
        # есть ли такая связь в графе
        for existing_link in self._links:
            if existing_link == link:return     #ничё не делаем

        self._links.append(link)    # +новую связь
        self.add_vertex(link.v1)    # +первую вершину связи
        self.add_vertex(link.v2)    # +вторую вершину связи
        if link not in link.v1.links: link.v1.links.append(link)    # +связь к списку связей первой вершины
        if link not in link.v2.links: link.v2.links.append(link)    # +связь к списку связей второй вершины

    def find_path(self,start_v:Vertex,stop_v:Vertex) -> Tuple[List[Vertex],List[Link]]:
        distances: Dict[Vertex,float]={}    # для хранения кратчайших расстояний до вершин
        previous: Dict[Vertex,Tuple[Optional[Vertex],Optional[Link]]]={}    # для хранения предыдущих вершин и связей в пути

        distances[start_v]=0    # начало
        previous[start_v]=(None,None)

        # Используем кучу (min-heap) для алгоритма Дейкстры, начинаем с начальной вершины с расстоянием 0
        heap=[(0,start_v)]

        while heap:    # Пока куча не пуста
            current_dist, current_vertex = heapq.heappop(heap)    # Извлекаем вершину с наименьшим расстоянием из кучи

            if current_vertex==stop_v:break    # конеч вершина

            if current_dist>distances.get(current_vertex,float('inf')):continue #пропускаем с большим расстоянием

            for link in current_vertex.links:    # Перебираем все связи текущей вершины
                neighbor =link.get_other_vertex(current_vertex)
                new_dist =current_dist+link.dist

                if new_dist<distances.get(neighbor,float('inf')):  # нашли путь короче
                    distances[neighbor] = new_dist
                    previous[neighbor] = (current_vertex,link)     # Сохраняем информацию о предыдущей вершине и связи
                    heapq.heappush(heap,(new_dist,neighbor))


        path_vertices: List[Vertex]=[]    # путь от конеч к начальной
        path_links: List[Link]=[]

        current = stop_v

        while current is not None:    # Пока не дойдем до начальной вершины
            # +текущую в путь
            path_vertices.append(current)
            if current in previous and previous[current][1] is not None:
                path_links.append(previous[current][1])    # +её связь в путь
            current = previous.get(current,(None,None))[0] #идёём дальше

        # Переворачиваем списки (из начала в конец
        path_vertices.reverse()
        path_links.reverse()

        return path_vertices, path_links #кортеж


class Station(Vertex):
    """    Класс для описания станций метро    """

    def __init__(self,name:str)->None:
        super().__init__()
        self.name=name
    def __str__(self)->str:return self.name
    def __repr__(self)->str:return self.name


class LinkMetro(Link):
    """    Класс для описания связей между станциями метро    """
    def __init__(self,v1:Station,v2:Station,dist:int)->None:
        super().__init__(v1,v2,dist)



if __name__ == "__main__":
    map_graph = LinkedGraph()

    v1 = Vertex()
    v2 = Vertex()
    v3 = Vertex()
    v4 = Vertex()
    v5 = Vertex()
    v6 = Vertex()
    v7 = Vertex()

    map_graph.add_link(Link(v1, v2))
    map_graph.add_link(Link(v2, v3))
    map_graph.add_link(Link(v1, v3))

    map_graph.add_link(Link(v4, v5))
    map_graph.add_link(Link(v6, v7))

    map_graph.add_link(Link(v2, v7))
    map_graph.add_link(Link(v3, v4))
    map_graph.add_link(Link(v5, v6))

    print(len(map_graph._links))  # 8 связей
    print(len(map_graph._vertex))  # 7 вершин
    path = map_graph.find_path(v1, v6)



map2 = LinkedGraph()
v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()
map2.add_link(Link(v1, v2))
map2.add_link(Link(v2, v3))
map2.add_link(Link(v2, v4))
map2.add_link(Link(v3, v4))
map2.add_link(Link(v4, v5))
assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"
map2.add_link(Link(v2, v1))
assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"
path = map2.find_path(v1, v5)
s = sum([x.dist for x in path[1]])
assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"
assert issubclass(Station, Vertex) and issubclass(LinkMetro, Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"
map2 = LinkedGraph()
v1 = Station("1")
v2 = Station("2")
v3 = Station("3")
v4 = Station("4")
v5 = Station("5")
map2.add_link(LinkMetro(v1, v2, 1))
map2.add_link(LinkMetro(v2, v3, 2))
map2.add_link(LinkMetro(v2, v4, 7))
map2.add_link(LinkMetro(v3, v4, 3))
map2.add_link(LinkMetro(v4, v5, 1))
assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"
path = map2.find_path(v1, v5)
assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
s = sum([x.dist for x in path[1]])
assert s == 7, "неверная суммарная длина маршрута для карты метро"