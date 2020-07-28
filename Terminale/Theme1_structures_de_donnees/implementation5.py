class Temps:
    
    def __init__(self, heures, minutes, secondes):
        self.h = heures
        self.m = minutes
        self.s = secondes
    
def heures(t):
    return t.h

def minutes(t):
    return t.m

def secondes(t):
    return t.s

def ajouter(t1, t2):
    h = t1.h + t2.h
    m = t1.m + t2.m
    s = t1.s + t2.s
    if s >= 60:
        s = s - 60
        m = m + 1
    if m >= 60:
        h = h + 1
        m = m - 60
    return Temps(h, m, s)

def soustraire(t1, t2):
    h = t1.h - t2.h
    m = t1.m - t2.m
    s = t1.s - t2.s
    if s < 0:
        s = 60 + s
        m = m - 1
    if m < 0:
        m = 60 + m
        h = h - 1        
    return Temps(h, m, s)

def egal(t1, t2):
    return t1.h == t2.h and t1.m == t2.m and t1.s == t2.s

def afficher(t):
    print(str(t.h) + ":" + str(t.m) + ":" + str(t.s))