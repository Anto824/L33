from ess import mix_list


def est_triee(L): #meilleure version
    for i in range(1,len(L)):
        if L[i]<L[i-1]:
            return False
    return True

def stupid_sort(lst):
    a = 0
    while not est_triee(lst):
        a+=1
        lst = mix_list(lst)
    print(a)
    return lst


L = [3,2,5,7,1,10,8,23,100]
#print(stupid_sort(L))


def tri_insertion(T):
    n = len(T)
    for i in range(1,n-1):
        x = T[i]
        j = i
        while j>0 and T[j-1]>x:
            T[j] = T[j-1]
            j-=1
        T[j] = x
    return T

#print(tri_insertion(L))

