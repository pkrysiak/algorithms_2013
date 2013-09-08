# select sort 

def select_sort(l):
    for i in range(len(l)):
        m = l[i]
        min_index = i
        for j in range(i+1,len(l)):
            if l[j]< m:
                m = l[j]
                min_index = j
        pom = l[i]
        l[i] = m
        l[min_index] = pom
    print l