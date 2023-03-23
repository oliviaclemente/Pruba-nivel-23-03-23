import math
math.sqrt(9)

class punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
print(punto)
    
def cuadrante(self):
    if self.x>0 and self.y>0:
        return "El punto {} está en el 1r cuadrante"
    if self.x<0 and self.y>0:
        return "El punto {} está en el 2n cuadrante"
    if self.x<0 and self.y<0:
        return "El punto {} está en el 3r cuadrante"
    if self.x>0 and self.y<0:
        return "El punto {} está en 4t cuadrante"
print(cuadrante)
    
def vector(self, dif_punto):
    vx= dif_punto.x - self.x
    vy= dif_punto.y - self.y
    return "El vector es ({}, {})".format(vx, vy)
print(vector)
   
def distancia(self, dif_punto):
    distancia= math.sqrt((dif_punto.x - self.x)**2 + (dif_punto.y - self.y)**2)
    return distancia
print(distancia)

print("d= sqrt((x2 - x1)**2 + (y2 -y1)**2)")

