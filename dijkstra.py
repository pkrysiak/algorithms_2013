# -*- coding: utf-8 -*-

INFINITY = 100001
def get_input():
    graph = {
         1 : {2:2, 6:1, 5:3, 4:5},
         4 : {1:5, 3:4, 5:4},
         2 : {6:2, 3:5, 1:2},
         3 : {5:4, 4:4, 2:5},
         5 : {6:3, 1:3, 4:4, 3:4},
         6 : {1:1, 2:2, 5:3}
         }
    return graph

def dijkstra(graph, start = 1):
    
    distance = {key : INFINITY for key in graph.keys()}
    distance[start] = 0

    parent = {key : None for key in graph.keys()}
    parent[start] = 0
    
    visited = {key : False for key in graph.keys()}
    visited[start] = True
    
    res = [(start,distance[start])]
    
    while False in visited.values():
        current_vert, current_dist = min(res, key = lambda x : x[1])
        res.remove((current_vert, current_dist))
        visited[current_vert] = True
        for neighbor, weight in graph[current_vert].items():
            if distance[neighbor] > distance[current_vert] + weight:
                distance[neighbor] = distance[current_vert] + weight
                parent[neighbor] = current_vert
                res.append((neighbor, weight))
    print distance.values()[1:]
    
dijkstra(get_input())
