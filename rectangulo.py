from math import fabs

class rectangulo():
    
    def __init__ (self, p1, p2):
        self.p1= p1
        self.p2= p2
        if p1 is None:
            p1= (0,0)
        if p2 is None:
            p2= (0,0)
    
    def base():