def full_name(str_arg):
    name = str_arg.split()
    a = name[0].upper()
    b = name[1].capitalize()
    return a +" " + b

def is_mail(str_arg):
    if "@" not in str_arg:
        return [0,2]
    else:
        str1 = str_arg.split("@")
        a = str1[0]
        b = str1[1]
        if len(a) == 0:
            return [0,1]
        elif a[0] == "." or a[-1] == ".":
            return [0,1]
        elif ".." in a:
            return [0,1]
        elif ".." in b or "--" in b:
            return [0,3]
        elif b[-1] == "." or "." not in b:
            return [0,4]
        else:
            return [1,0]

#test = ['bisgambiglia_paul@univ-corse.fr','bisgambiglia_paulOuniv-corse.fr','bisgambiglia_paul@univ-corsePOINTfr','@univ-corse.fr']
#for i in test:
    print(is_mail(i))

