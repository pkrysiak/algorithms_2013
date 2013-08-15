# -*- coding: utf-8 -*-

'''
Iteracyjne wyszukiwanie binarne elementu w ciągu niemalejącym.
'''


def binary_search(a, x, lo=None, hi=None):
    if hi is None:
        hi = len(a)
    if lo is None:
        lo = 0
    while lo < hi:
        mid = (lo+hi)//2 #floor division
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    raise ValueError('Nie znaleziono podanego klucza')
    
    
print binary_search([1,1,3,5,6,8], 4)