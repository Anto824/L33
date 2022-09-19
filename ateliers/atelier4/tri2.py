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



def tri_selection(a):
    for i in range(len(a)-1):
        minimum= a[i:].index(min(a[i:]))
        a[i], a[i+minimum] = a[i+minimum], a[i]
    
    return a

def tri_bulle(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            
    return a

def fusion(l, r):
    n = len(l + r) #Taille du tableau après la fusion
    s = max(l + r) + 1 #Garde

    l.append(s)
    r.append(s)

    a = []
    while len(a) < n:
        a.append(l.pop(0)) if l[0] <= r[0] else a.append(r.pop(0))
    
    return a

def tri_fusion(a):
    if len(a) == 1:
        return a

    mid = len(a) // 2
    l = tri_fusion(a[:mid])
    r = tri_fusion(a[mid:])
    
    return fusion(l, r)



