# -*- coding: utf-8 -*-

'''
Dynamiczna implementacja dwumianu newtona.
'''
from exceptions import IOError

def get_values(n=1,k=1):
    n = int(input('podaj n: '))
    k = int(input('podaj k: '))
    if k > n:
        raise IOError('k musi być większe równe n!')
    return (n,k)

def show_tab(tab):
    for i in tab:
        print i

def newton_binomial((n,k)):
    tab = [[0 for x in range(n+1)] for y in range(n+1)]
    
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if j == 0 or j == i:
                tab[i][j] = 1
            else:
                tab[i][j] = tab[i-1][j-1] + tab[i-1][j]
#     show_tab(tab) 
    return tab[n][k]
    
print newton_binomial(get_values())