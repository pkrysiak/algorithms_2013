# -*- coding: UTF-8 -*-
"""
TASK:
Dany jest skierowany graf ważony. Znajdź najkrótsze odległości do wszystkich wierzchołków z jednego wyróżnionego wierzchołka s.
Wejście

W pierwszym wierszu dane są liczby n, m , s, gdzie n ≤ 500, m ≤ 500*500, 0 ≤ s ≤ n, oznaczające odpowiednio liczbę wierzchołkó, liczbę krawędzi i numer wierzchołka wyróżnionego. Następnie na wejściu podanych jest m wierszy zawierających po trzy liczby całkowite a, b, ,c, gdzie liczby 0 ≤ a,b ≤ n, -1 000 000 ≤ c ≤ 1 000 000, oznaczające krawędż skierowaną od wierzchołka a do wierzchołka b o koszcie c.
Wyjście

Jeśli w grafie istnieje cykl o ujemnym łącznym koszcie, to należy wypisać słowo NIE. W przeciwnym wypadku, należy wypisać odległości do wszystkich wierzchołków osiągalnych z wierzchołka s w kolejności od najmniejszego numeru (podając najpierw numer wierzchołka a za nim --- odległość), z tym, że nie należy wypisywać odległości do wierzchołka wyróżnionego.
Przykład

Dla danych wejściowych
3 2 1
0 1 10
1 2 20
poprawną odpowiedzią jest
2 20
"""

class GraphHasCycleError(Exception):
    pass

def get_input():
    inf = 1000001
    n = int(raw_input('n (number of vertices): '))
    m = int(raw_input('m (number of edges): '))
    s = int(raw_input('s (start vertex): '))
    print n,m,s
    distance = {} # oszacowania odległości wag od startu do każdego wierzchołka
    parent = {} # poprzednicy dla każdego wierzchołka
    graph = {} # krawędź 1: { 2:3, 5:4 } znaczy 1 --(3)--> 2, 1 --(4)--> 5, ( skąd ---(waga)---> gdzie ) 
    for node in range(m):
        start, end, weight = [int(x) for x in raw_input('start end weight: ').split(' ')]
        if not graph.has_key(start):
            graph[start] = { end : weight }
        else:
            graph[start][end] = weight
            
        if not graph.has_key(end):
            graph[end] = {}
        
        distance[start] = 0
        distance[end] = 0
        parent[start] = None
        parent[end] = None
        if start != s:
            distance[start] = inf
        if end != s:
            distance[end] = inf
    return graph, distance, parent, s

def bellman_ford():
    graph, distance, parent, s= get_input()
    for i in range(len(graph)-1): # tyle przebiegów wystarczy aby obliczyć wszystkie najkrótsze ścieżki
        for start_vert in graph:
            for end_vert in graph[start_vert]:
                  if distance[end_vert] > distance[start_vert] + graph[start_vert][end_vert]:
                      distance[end_vert] = distance[start_vert] + graph[start_vert][end_vert]
                      parent[end_vert] = start_vert
    
    for start_vert in graph:
        for end_vert in graph[start_vert]:
           if distance[start_vert] + graph[start_vert][end_vert] < distance[end_vert]:
               raise GraphHasCycleError('Znaleziono cykl.') 
    return distance, parent, graph, s
    
def show_result():
    distance, parent, graph, s = bellman_ford()
    for vert, shortest_path in distance.items():
        if vert != s and not graph[vert].has_key(s):
            print vert, shortest_path

show_result()         
                        
