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
    s = secondes(t1) + secondes(t2)
    m = minutes(t1) + minutes(t2)
    h = heures(t1) + heures(t2)
    if s >= 60:
        s = s - 60
        m = m + 1
    if m >= 60:
        m = m - 60
        h = h + 1        
    return [h, m, s]

def soustraire(t1, t2):
    """temps x temps --> temps
    Renvoie la différence t1 - t2, où t1 >= t2"""
    assert t1 >= t2, "le premier temps doit être supérieur au second"
    s = secondes(t1) - secondes(t2)
    m = minutes(t1) - minutes(t2)
    h = heures(t1) - heures(t2)
    if s < 0:
        s = 60 + s
        m = m - 1
    if m < 0:
        m = 60 + m
        h = h - 1        
    return [h, m, s]

def egal(t1, t2):
    return t1 == t2

def afficher(t):
    print(str(t[0]) + ":" + str(t[1]) + ":" + str(t[2]))