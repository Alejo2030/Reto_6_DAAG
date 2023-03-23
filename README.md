# Reto_6_DAAG
Desarrollo del reto 6, Daniel Archila; programación de computadores!!



## Ejercicios 
 ***°Ley de la gravedad***
 
```ruby
 : float 
G = 6.67384e-11

def fuerza_gravedad_entre_dos_objetos(masa1, masa2, distancia):
    fuerza = G * (masa1 * masa2) / distancia**2
    return fuerza

if __name__ == "__main__":
    m1 = float(input("Ingrese la masa en Kilogramos del primer objeto: "))
    m2 = float(input("Ingrese la masa en Kilogramos del segundo objeto: "))
    d = float(input("Ingrese la distancia en metros que los separa: "))

    fuerza_gravedad = fuerza_gravedad_entre_dos_objetos(m1, m2, d)

    print("La fuerza de gravedad entre los dos objetos es:", fuerza_gravedad, "Newtons")
```
    
