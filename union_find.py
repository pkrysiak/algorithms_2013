# -*- coding: utf-8 -*- 
# Union find structure
from Queue import deque

class Item(object):
    '''
    Obiekt który będzie opakowany w obiekt UFItem.
    Może być czymkolwiek.
    '''
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return str(self.value)
        
class UnionFind(object):
    '''
    Klasa UnionFind.
    Udostępnia dwie metody: union, find.
    find - Wyznacza, w którym zbiorze jest dany element, pozwalając na sprawdzenie, czy dwa elementy są w tym samym zbiorze.
    union - Łączy dwa zbiory w jeden.
    Wyjaśnienie: 
    http://www.rafalnowak.pl/wiki/index.php?title=UNION_FIND
    '''
    __ITEMS = {} # mapowanie Item -> UFItem
    __root = None # tymczasowy korzeń drzewa 
    
    class UFItem(object):
        '''
        Klasa opakowywująca obiekt 'obj'. 
        Dodaje dwa dodatkowe parametry (parent,rank).
        Przykłady użycia:
        l = [ 
             Item(1),
             Item(2),
             Item(3),
             Item(10)
        ]
        u = UnionFind(l)
        print u.union(l[0], l[1])
        print u.find(l[2]).show()
        '''
        def __init__(self, obj, parent = None, rank = 0):
            self.parent = parent # parent object (Type : UFItem)
            self.rank = rank # rank (Type : Int)
            self.obj = obj # object (Type : Item)
        
        def show(self):
            '''
            metoda pokazująca pola obiektu.
            '''
            if self.parent:
                return (self.parent.show(), self.rank, self.obj)
            else:
                return (self.parent, self.rank, self.obj)
    
    def __init__(self, item_list):
        self._load_items(item_list)
            
    def _load_items(self, item_list):
        for item in item_list:
            self.__ITEMS[item] = self.UFItem(item)

    def find(self, item):
        '''
        Find.
        Przyjmuje obiekt Item().
        Zwraca reprezentanta szukanego elementu.
        '''
        elem = self.__ITEMS[item]
        d = deque()
        while elem.parent: # przejście do korzenia
            d.append(elem) # odkładanie na stos
            elem = self.__ITEMS[elem.parent.obj]
        root = elem
        while len(d) > 0: # kompresja ścieżki
            elem = d.pop()
            elem.parent = root
        return root
    
    def union(self, Item1, Item2):
        '''
        Union. 
        Przyjmuje dwa argumenty typu Item. 
        Łączy dwa elementy wg ich rangi.
        '''
        UFItem1 = self.find(Item1)
        UFItem2 = self.find(Item2)
        if UFItem1.obj != UFItem2.obj:
            if UFItem1.rank < UFItem2.rank:
                UFItem1.parent = UFItem2
            elif UFItem1.rank < UFItem2.rank:
                UFItem2.parent = UFItem1
            elif UFItem1.rank == UFItem2.rank:
                UFItem1.parent = UFItem2
                UFItem2.rank += 1
            return True
        else:
            return False
