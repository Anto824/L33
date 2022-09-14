from random import *
from re import M

#print(random())

def gen_list_random_int(borneinf,bornesup):
    lst = []
    n = input('combien de nombres voulez vous ? ')
    if n <=0 or n == None:
        n = 10
    for i in range (n-1):
        lst.append(randint(borneinf,bornesup))

    
def mix_list(liste_to_mix):
    taux_melange = randint(len(liste_to_mix),len(liste_to_mix)*2)
    for i in range(len(liste_to_mix)):
        n = randint(0,len(liste_to_mix)-1)
        m = randint(0,len(liste_to_mix)-1)
        x = liste_to_mix[m]
        liste_to_mix[m] = liste_to_mix[n]
        liste_to_mix[n] = x
    return liste_to_mix



L = [1,2,3,4,5,6,7,8,9,10]
#print(mix_list(L))



def extract_elements_list(list_in_which_to_choose,int_nbr_element_to_extract):
    lst = []
    for i in range(int_nbr_element_to_extract):
        lst = list_in_which_to_choose.pop(choice(list_in_which_to_choose))
    return lst



