


def present(L,e):
    return e in L


def test_present(present:callable):
    if present([],2):
        print("SUCCES : Test liste vide")
    else:
        print("ECHEC : test liste vide")
    L = [1,2,3,4,5,6,7,8,9,10]
    if present(L,1):
        print("SUCCES : test debut")
    else:
        print("ECHEC : test debut")
    if present(L,10):
        print("SUCCES : test fin")
    else:
        print("ECHEC : test fin")
    if present(L,5):
        print("SUCCES : test milieu")
    else:
        print("ECHEC : test milieu")
    if present(L,0):
        print("ECHEC : test absence")
    else:
        print("SUCCES : test absence")


    
