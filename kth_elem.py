# -*- coding: utf-8 -*-
# algorytm znajdujący k-ty co do wielkości element ciągu
# wykorzystuje algorytm magicznych piątek
# nieco nieoszczędna implementacja


def magic_five(data, k):
    '''
    Algorytm znajdujący k-ty co do wielkości element w zbiorze.
    Wykorzystuje algorytm magicznych piątek do znajdywania median.
    '''
    if len(data) < 5:
        return sorted(data)[k]
    else:
        hr = len(data)%5
        if hr == 0:
            listcount = len(data)/5 # ile list z piątkami
        else:
            listcount = (len(data)/5)+1
            
    five_lists = [[] for i in range(listcount)] # lista pustych list gdzie mają być piątki
    which_list = 0
    for i in range(len(data)):
        if i!=0 and i%5 == 0:
            which_list += 1
        five_lists[which_list].append(data[i])  # uzupełnianie list z piątkami
        
    pre_M = [sorted(i) for i in five_lists] # posortowane piątki
    
    M = [j[len(j)/2] for j in pre_M] # mediany z piątek
    
    m = magic_five(M,int(len(M)/2.0))
    A_m = []
    A_r = []
    A_w = []
    for i in data:
        if i > m :
            A_w.append(i)
        elif i < m:
            A_m.append(i)
        else:
            A_r.append(i)
        
    if len(A_m) >= k:
        return magic_five(A_m,k)
    elif len(A_m)+len(A_r) >= k:
        return m
    else:
        return magic_five(A_w,k-len(A_m)-len(A_r))
    
print magic_five([3,2,4,1,8,9,11,14,15,18,22,45,23], 4)
