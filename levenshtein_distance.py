# -*- coding: utf-8 -*-
# wyjaśnienie: http://www.algorytm.org/przetwarzanie-tekstu/odleglosc-levenshteina-odleglosc-edycyjna.html

def levenshtein_distance(word1, word2):
    '''
        funkcja obliczająca odległość edycyjną dwóch słów.
        programowanie dynamiczne.
    '''
    tab = [[w1_x if w2_y == 0 else 0 for w1_x in range(len(word1)+1)] for w2_y in range(len(word2)+1)] # tablica z wypełnionym pierwszym wierszem
    for y in range(len(tab)):
        tab[y][0] = y #wypełnienie pierwszej kolumny

    for y in range(1,len(tab)):
        for x in range(1,len(tab[0])):
            up = tab[y-1][x]
            left = tab[y][x-1]
            diagonal = tab[y-1][x-1]
            cost = 0 if word1[x-1] == word2[y-1] else 1
    
            current = min(
                          up + 1,
                          left + 1,
                          diagonal + cost
                          )
            tab[y][x] = current
    return tab[-1][-1]
    
print levenshtein_distance('kotka', 'foka')