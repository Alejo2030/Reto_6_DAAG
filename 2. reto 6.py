import math


def area_figura (b:float, a:float, r:float, ) -> float:
    area_rectangulo = b * a
    area_de_las_ruedas = (math.pi * r**2) * 2
    return area_rectangulo + area_de_las_ruedas

def perimetro_figura(b:float, a:float , r:float, ) -> float:
    perimetro_rectangulo = a*2 + b*2
    rueda= r * math.pi * 2
    return perimetro_rectangulo + rueda * 2  


if __name__ == '__main__':
    b = float(input("Ingresar base del rectangulo en cm: "))
    a = float(input("Ingresar la altura del rectangulo en cm: "))
    r = float(input("Ingresar el radio de las ruedas en cm: "))
   
    p = perimetro_figura(b, a, r)
    a = area_figura(b, a, r )
    print(" El perimetro de la figura es  " + str(p) + " cm")
    print(" El area de la figura es : " + str(a) + " cm^2")