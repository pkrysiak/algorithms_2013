#-*- coding: utf-8 -*-
# longest common subsequence

def LCS(word1 = 'markotny',word2 = 'romantyk', mode=False):
    '''
        Funkcja obliczająca LCS dwóch ciągów znaków.
        wyjaśnienie: http://informatyka.wroc.pl/node/627
        mode - False : pokazuje długość ciągu)
        mode - True : pokazuje przykładowy ciąg
    '''
    # tablica dwuwymiarowa gdzie na górze znajduje się słowo word1 a na po lewej word2
    lcs_tab = [ 
                  [None for x in range(len(word1)+1)] for y in range(len(word2)+1)
              ]
    
    for i in lcs_tab: # dla pierwszej kolumny i pierwszego wiersza zerujemy bo lcs zerowego prefiksu i jakiegokolwiek słowa jest równy 0
        i[0] = 0
    for i in range(len(lcs_tab[0])):
        lcs_tab[0][i] = 0

    #zliczamy
    for i in range(1,len(lcs_tab)):
        for j in range(1,len(lcs_tab[0])):
            if word2[i-1] == word1[j-1]:
                lcs_tab[i][j] = lcs_tab[i-1][j-1] + 1 # jeśli poprzednie znaki są równe to zwiększami licznik
            else:
                lcs_tab[i][j] = max(lcs_tab[i-1][j],lcs_tab[i][j-1]) # jeśli nie to przepisujemy większą wartość
                
    def retrieve_lcs():
        '''
            Funkcja odtwarzająca jeden z możliwych LCS-ów.
        '''
        pointer_x = len(lcs_tab[-1])-1 # "wskaźnik" na koniec listy1 ( odpowiadającej wyrazowi1 )
        pointer_y = len(lcs_tab)-1     # "wskaźnik" na koniec listy2 ( odpowiadającej wyrazowi2 )
        result = ''
        while pointer_x >0 and pointer_y>0: # stop kiedy przejdziemy przez cały wyraz
            up = lcs_tab[pointer_y-1][pointer_x] # element powyżej obecnego
            left = lcs_tab[pointer_y][pointer_x-1] # element po lewej od obecnego
            x_letter = word1[pointer_x-1] # litera odpowiadająca obecnej pozycji w pierwszym wyrazie
            y_letter = word2[pointer_y-1] # litera odpowiadająca obecnej pozycji w drugim wyrazie
            if x_letter == y_letter: 
                pointer_x-=1
                pointer_y-=1
                result = x_letter + result # jeśli litery są te same w obu wyrazach to dodajemy do wyniku 
            else:   # jeśli nie to przechodzimy na pole które ma większą wartość 
                if left > up:
                    pointer_x-=1 # w lewo 
                elif left <= up:
                    pointer_y-=1 # do góry
        return result
        
    if mode:
        return retrieve_lcs()
    else:
        return lcs_tab[-1][-1]
    
print LCS(mode=True)