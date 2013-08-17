#-*- coding: utf-8 -*- 

def binary_search_modified(items_list, elem, lo=0, hi=None):
    '''
        Zwraca miejsce w którym ma być wstawiony element.
        Jeśli element jest w zbiorze, zwraca kolejny indeks za tym elementem (linia 19)
        Jeśli elementu nie ma w zbiorze, zwraca kolejny indeks za elementem który jest mniejszy od wstawianego ( linia 22)
    '''
    if hi is None:
        hi = len(items_list)
    while lo < hi:
        mid = (lo+hi)//2
        midval = items_list[mid]
        if midval < elem:
            lo = mid+1
        elif midval > elem: 
            hi = mid
        else:
            return mid+1
    if lo==hi:
        return lo+1
    
def longest_increasing_subsequence(items_list, show=False):
    '''
        funkcja obliczająca jaki jest najdłuższy rosnący podciąg, w liście items_list
        in: list, bool
        out: int/list
        -------
        Zwraca długość LIS lub przykładowy LIS w zależności od zmiennej show.
    '''
    items_list.insert(0,1000) # sztucznie dostawiony element na miejsce 0 aby indeksy zaczynały się od 1
    dic = {}
    backs = [] # lista ostatnich elementów w warstwie
    lis =[]
    for i in range(1, len(items_list)):
        index = binary_search_modified(backs, items_list[i]) # znajdujemy jakiej długości ciąg może przedłużyć dany element ( do jakiej warstwy go wstawić )
        if not dic.has_key(index):              # tworzymy warstwę jeśli jej nie ma
            dic[index] = [ (items_list[i], i) ] # dodajemy parę ( element, index elementu w ciągu wejściowym ) drugi element krotki będzie potrzebny przy odtwarzaniu.
        else:
            dic[index].append( (items_list[i], i) )
        backs = [ dic[i][-1][0] for i in dic ] 
    
    lenght = len(dic.keys())    # ilość warstw
    
    def show_lis():
        '''
            Podmetoda odtwarzająca przykładowy ciąg o podanej długości.
            Zasada działania:
                Dodawaliśmy jako drugi element krotki indeksy dodawanych elementów aby teraz z nich skorzystać.
                Zaczynając od ostatniego elementu ostatniej warstwy bierzemy zachłannie element którego indeks 
                w ciągu wejściowym jest mniejszy od indeksu elementu aktualnie przetwarzanego.
                W ten sposób nigdy nie pomylimy kolejności elementów. 
        '''
        lenght = len(dic.keys())
        last_elem = dic[lenght][-1] # ostatni element ostatniej warstwy ( przykładowy element od którego zaczniemy zwijać LIS )
        ind = last_elem[1]          # indeks powyższego elementu ( który jest krotką )
        lis.append(last_elem[0])
        
        while (lenght>0):           # idziemy po wszystkich warstwach
            current_list_len = len(dic[lenght]) # długość aktualnie rozpatrywanej warstwy
            while current_list_len>0:   # przeglądamy warstwę od tyłu
                cind = dic[lenght][current_list_len-1][1]   # indeksy poszczególnych elementów w warstwie 
                elem = dic[lenght][current_list_len-1][0]   # wartość poszczególnych elementów w warstwie
                if cind < ind:
                    lis.append(elem)    # jeśli napotkamy na element którego indeks w ciągu wejściowym jest mniejszy od indeksu aktualnie rozpatrywanego elementu to dodajemy go do listy
                    ind = cind          # przestawiamy indeksy
                    break
                current_list_len-=1
            lenght-=1
        return lis
    
    if not show:
        return lenght
    else:
        return show_lis()
    
print longest_increasing_subsequence([3,4,2,3,7,6,5,6,8,5,9,4], show=True)
