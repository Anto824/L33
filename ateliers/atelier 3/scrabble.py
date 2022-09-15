from motcroise import mots_Nlettres
from pendu import build_list



def mot_correspondant(mot,motif):
    if len(mot) != len(motif):
        return False
    for i in range(len(mot)):
        if motif[i]!=".":
            if motif[i] != mot[i]:
                return False
    return True



def presente(lettre,mot):
    if lettre in mot:
        return mot.index(lettre)
    else:
        return False

def mot_possible(mot,lettres):
    for i in mot:
        if mot.count(i) != lettres.count(i):
            return False
    return True


def mot_optimaux(dico,lettres):
    ll = build_list(dico)
    lst = []
    llst = []
    for i in ll:
        if mot_possible(i,lettres):
            lst.append(i)
    for i in range(len(lettres),0,-1):
        llst = mots_Nlettres(lst,i)
        if llst != []:
            return llst
        else:
            print(llst)
            print('aucun mot trouvé')


print(mot_optimaux('ateliers/atelier 3/littre.txt','abcehuva'))


