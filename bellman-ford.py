# -*- coding: UTF-8 -*-
from curses.has_key import has_key

def get_input():
    n = int(raw_input('n: '))
    m = int(raw_input('m: '))
    s = int(raw_input('s: '))
    print n,m,s
    d = {}
    p = {}
    graph = {} # node 1: { 2:3, 4:5 } means 1--(3)-->2, 1--(4)-->5, graph is dictionary of dictionaries 
    for node in range(m):
        a,b,c = [int(x) for x in raw_input('a b c: ').split(' ')]
        if not graph.has_key(a):
            graph[a] = { b:c }
            p[a] = None
            if a != s:
                d[a] = 1000001
            else:
                d[a] = 0
        else:
            graph[a][b] = c 
    return graph,d,p

def bellman_ford():
    g,d,p = get_input()
    for i in range(len(g)-1):
        for start_vert in g:
            for end_vert in g[start_vert]:
                  if d[end_vert] > d[start_vert] + g[start_vert][end_vert]:
                      d[end_vert] = d[start_vert] + g[start_vert][end_vert]
                      p[end_vert] = start_vert
    
    for start_vert in g:
        for end_vert in g[start_vert]:
           if d[start_vert] + g[start_vert][end_vert] < d[end_vert]:
               return None     
    
    return (d,p)
                      
                      
print bellman_ford()  