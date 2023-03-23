from math import fabs

class rectangulo():
    
    def __init__ (self, p1, p2):
        self.p1= p1
        self.p2= p2
        if p1 is None:
            p1= (0,0)
        if p2 is None:
            p2= (0,0)
    
    def base(self):
        return fabs(self.p1.x - self.p2.x)
        
    def altura(self):
        return fabs(self.p1.y - self.p2.y)
        
    def area(self):
        return self.base() * self.altura()