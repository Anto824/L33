


def mots_Nlettres(lst_mot,n):
    lst = []
    for i in lst_mot:
        if len(i) == n:
            lst.append(i)
    return lst


lst_mot = ['jouer','bonjour',"punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", "finir", "aimer"]

#print(mots_Nlettres(lst_mot,5))


def commence_par(mot,prefixe):
    return mot[0] == prefixe

def finit_par(mot, suffixe):
    return mot[-1],suffixe


def finissent_par(lst_mot,suffixe):
    lst = []
    for i in lst_mot:
        if finit_par(i,suffixe):
            lst.append(i)
    return lst

def commencent_par(lst_mot,prefixe):
    lst = []
    for i in lst_mot:
        if commence_par(i,prefixe):
            lst.append(i)
    return lst


def liste_mots(lst_mot,prefixe,suffixe,n):
    lst = []
    for i in lst_mot:
        if commence_par(i,prefixe) and finit_par(i,suffixe) and len(i) == n:
            lst.append(i)


def dictionnaire(fichier):
    lst = []
    f = open(fichier,"r")
    c = f.readline()
    while c!="":
        lst.append(c)
        #print(c,end="")
        c = f.readline()
    return lst





