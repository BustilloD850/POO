def area():
    altura=int(input("Ingrese la altura del rectangulo: "))

    base=int(input("Ingrese la base del rectangulo: "))
    area= (altura*base)/2
    return area

print(area())

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
rect = Rectangulo(5,3)
print(rect.area())