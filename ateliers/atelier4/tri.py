def tri(L,debut,fin):
    if debut < fin:
        i = partition(L,debut,fin)
        tri(L,debut,i-1)
        tri(L,i+1,fin)
    return L

def partition(L,debut,fin):
    pivot = L[fin]
    i = debut
    j = debut
    while j < fin:
        if L[j] <= pivot:
            L[i],L[j] = L[j],L[i]
            i += 1
        j += 1
    L[fin],L[i] = L[i],L[fin]
    return i




L = [8,2,3,9,6,10,13,4]

print(tri(L,0,len(L)-1))
