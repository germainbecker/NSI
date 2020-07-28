def Temps(h, m, s):
    """Entier x Entier x Entier --> Temps"""
    return [h, m, s]
    
def heures(t):
    """Temps --> Entier"""
    return t[0]

def minutes(t):
    """Temps --> Entier"""
    return t[1]

def secondes(t):
    """Temps --> Entier"""
    return t[2]
    
def ajouter(t1, t2):
    """Temps x Temps --> Temps"""
    secondes = temps_vers_int(t1) + temps_vers_int(t2)
    return int_vers_temps(secondes)

def soustraire(t1, t2):
    """temps x temps --> temps
    Renvoie la différence t1 - t2, où t1 >= t2"""
    assert t1 >= t2, "le premier temps doit être supérieur au second"
    secondes = temps_vers_int(t1) - temps_vers_int(t2)
    return int_vers_temps(secondes)

def egal(t1, t2):
    return t1 == t2

def afficher(t):
    print(str(t[0]) + ":" + str(t[1]) + ":" + str(t[2]))

def temps_vers_int(t):
    return t[0]*3600 + t[1]*60 + t[2]

def int_vers_temps(secondes):
    m, s = divmod(secondes, 60)
    h, m = divmod(m, 60)
    return [h, m, s]