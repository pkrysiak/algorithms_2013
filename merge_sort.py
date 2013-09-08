# merge sort 

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    r = lista[:len(lista)/2]
    l = lista[(len(lista)/2):]
    left = merge_sort(l)
    right = merge_sort(r)
    return merge(left, right)
    
def merge(left, right):
    res = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                res.append(left[0])
                left = left[1:]
            else:
                res.append(right[0])
                right = right[1:]
                
        elif len(left) > 0:
            res.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            res.append(right[0])
            right = right[1:]
    return res
    
l1 = [1]
l2 = [1,2]
l3 = [1,2,3,4]
l5 = [1,2,3,4,5]
l10 = [1,2,3,4,5,6,7,8,9,10]
l11 = [20,40,60]
print merge_sort([100,3,-2,50,3,4,5,10,12])
#print merge(l3,l5)