import random



def places_lettre(ch,mot):
    lst = []
    for i in range (len(mot)):
        if ch == mot[i]:
            lst.append(i)
    return lst


def testplace(lstmot,lstchar):
    for i in range (len(lstmot)):
        print(places_lettre(lstchar[i],lstmot[i]))

lstmot = ['bonjour','bonjour','maman']
lstchar = ['b','a','m']
#testplace(lstmot,lstchar)


def outputStr(mot,lpos):
    lst = []
    if lpos == []:
        for i in range(len(mot)):
            lst.append("_")
    else:
        for i in range(len(mot)):
            if i in lpos:
                lst.append(mot[i])
            else:
                lst.append("_")
    return lst

def testout(lstmot,lstlpos):
    for i in range (len(lstmot)):
        print(outputStr(lstmot[i],lstlpos[i]))

lstm = ['bonjour','bonjour','bonjour','bon','maman']
lstp = [[],[0],[0,1,4],[0,1,2],[1,3]]
#testout(lstm,lstp)


def runGame():
    #lstmot = ['bonjour','toto','titi','elephant','cheval','chat']
    mot = random.choice(difficulte('ateliers/atelier 3/capitales.txt'))
    print(outputStr(mot,[]))
    lst = []
    jouer = True
    nbErr = 0
    print("|")
    print("|")
    print("|")
    print("|")
    print("|_____")
    while jouer:
        inp = input('donnez une lettre: ')
        l = places_lettre(inp,mot)
        if l != []:
            for i in l:
                lst.insert(i,i)
        else:
            nbErr += 1
        print(outputStr(mot,lst))
        if len(lst) == len(mot):
            jouer = False
            print('felicitations, vous avez gagné')
        if nbErr == 0:
            print("|")
            print("|")
            print("|")
            print("|")
            print("|_____")
        elif nbErr == 1:
            print("|---]")
            print("|")
            print("|")
            print("|")
            print("|_____")
        elif nbErr == 2:
            print("|---]")
            print("|  O")
            print("|")
            print("|")
            print("|_____")
        elif nbErr == 3:
            print("|---]")
            print("|  O")
            print("|  T")
            print("|")
            print("|_____")
        elif nbErr == 4:
            print("|---]")
            print("|  O")
            print("|  T")
            print("| /")
            print("|_____")
        elif nbErr == 5:
            print("|---]")
            print("|  O")
            print("|  T")
            print("| / \\")
            print("|_____")
            jouer = False
            print('perdu, le mot était ', mot)
        



def build_list(file):
    f = open(file,"r")
    c = f.readlines()

    return c


def build_dict(file):
    f = build_list(file)
    a = []
    b = []
    c = []
    for i in f:
        if len(i)<7:
            a.append(i)
        elif len(i)>6 and len(i)<9:
            b.append(i)
        else:
            c.append(i)
    dico = {
        'facile' : a,
        'normal' : b,
        'difficile' : c
    }
    #print(dico)
    return dico

def difficulte(file):
    diff = input('quelle difficulté choisissez-vous ? easy, normal, difficile: ')
    dict = build_dict(file)
    if diff == 'easy':
        return dict['facile']
    elif diff == 'normal':
        return dict['normal']
    else:
        return dict['difficile']



runGame()




