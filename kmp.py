# -*- coding: utf-8 -*-
# KMP Algorithm

def construct_pi_table(pattern):
    '''
    Example of Pi table look for some pattern
    PATTERN = 'abbabcabb'
    |      | E | a | b | b | a | b | c | a | b | b |
    | i    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
    | P[i] | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 1 | 2 | 3 |
    '''
    Pi = [-1 for x in range(len(pattern) + 1)]
    Pi[0], Pi[1] = 0, 0 # pierwsze dwa elementy są zerami ponieważ pierwszy element to słowo puste a drugi element to pierwszy element tekstu
    t = 0
    for i in range(2, len(pattern) + 1):
        while t > 0 and pattern[t] != pattern[i - 1]: # jeśli trafiliśmy przedtem na pasujące znaki (t>0) a teraz znaki nie pasują to musimy się cofnąć Pi[t] 
            t = Pi[t]
        if pattern[t] == pattern[i - 1]: # jeśli trafimy na pasujące znaki inkrementujemy wskaźnik t
            t += 1
        Pi[i] = t #wypełniamy tablicę
    return Pi

def kmp_matcher(Text, Pattern):
    '''
    Algorytm KMP. Uzywa skonstruwanej wczesniej tabilicy pi aby szybko odnajdować wzorzec w tekście.
    
    Funkcja zwraca listę indeksów w których zaczyna sie wzorzec.
    '''
    Pi = construct_pi_table(Pattern)
    qc = 0
    pattern_indexes = []
    for i in range(len(Text)):
        while qc > 0 and Pattern[qc] != Text[i]:
            qc = Pi[qc]
        if Pattern[qc] == Text[i]:
            qc += 1
        if qc == len(Pattern):
            pattern_indexes.append(i - len(Pattern) + 1 )
            qc = Pi[qc]
    return pattern_indexes
    
    
    
    
