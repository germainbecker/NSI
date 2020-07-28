def Temps(h, m, s):
    """Entier x Entier x Entier --> temps"""
    return {"h": h, "m": m, "s": s}
    
def heures(t):
    """temps --> Entier"""
    return t["h"]

def minutes(t):
    """temps --> Entier"""
    return t["m"]

def secondes(t):
    """temps --> Entier"""
    return t["s"]
    
def ajouter(t1, t2):
    """temps x temps --> temps"""
    s = secondes(t1) + secondes(t2)
    m = minutes(t1) + minutes(t2)
    h = heures(t1) + heures(t2)
    if s >= 60:
        s = s - 60
        m = m + 1
    if m >= 60:
        m = m - 60
        h = h + 1        
    return {"h": h, "m": m, "s": s}

def soustraire(t1, t2):
    """temps x temps --> temps
    Renvoie la différence t1 - t2, où t1 >= t2"""
    assert (t1["h"], t1["m"], t1["s"]) >= (t2["h"], t2["m"], t2["s"]) , "le premier temps \
    doit être supérieur au second"
    s = secondes(t1) - secondes(t2)
    s = secondes(t1) - secondes(t2)
    m = minutes(t1) - minutes(t2)
    h = heures(t1) - heures(t2)
    if s < 0:
        s = 60 + s
        m = m - 1
    if m < 0:
        m = 60 + m
        h = h - 1        
    return {"h": h, "m": m, "s": s}

def egal(t1, t2):
    return t1 == t2

def afficher(t):
    print(str(t["h"]) + ":" + str(t["m"]) + ":" + str(t["s"]))