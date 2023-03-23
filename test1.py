import math
math.sqrt(9)
from punto import Punto


class test_punto():
    punto= Punto(2,3)
    assert punto.x == 2
    assert punto.y == 3
    print(punto)
    
def test_cuadrante(self):
    punto= Punto(2,3)
    if self.x>0 and self.y>0:
        return "El punto {} está en el 1r cuadrante"
    if self.x<0 and self.y>0:
        return "El punto {} está en el 2n cuadrante"
    if self.x<0 and self.y<0:
        return "El punto {} está en el 3r cuadrante"
    if self.x>0 and self.y<0:
        return "El punto {} está en 4t cuadrante"
print(test_cuadrante)
    
def test_vector(self, dif_punto):
    vx= dif_punto.x - self.x
    vy= dif_punto.y - self.y
    return "El vector es ({}, {})".format(vx, vy)
print(test_vector)
   
def test_distancia(self, dif_punto):
    distancia= math.sqrt((dif_punto.x - self.x)**2 + (dif_punto.y - self.y)**2)
    return distancia
print(test_distancia)

from math import fabs

class test_ectangulo():
    
    def test___init__ (self, p1, p2):
        self.p1= p1
        self.p2= p2
        if p1 is None:
            p1= (0,0)
        if p2 is None:
            p2= (0,0)
    
    def test_base(self):
        return fabs(self.p1.x - self.p2.x)
        
    def test_altura(self):
        return fabs(self.p1.y - self.p2.y)
        
    def test_area(self):
        return self.base() * self.altura()
    
