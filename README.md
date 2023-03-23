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
    
***Ejercicio: Uno de los módulos que trae python es math, hacer un porgrama en Python importando math y usar 5 de las funciones incluidas en este módulo.***


```ruby
import math

if __name__ == "__main__":

# Se ingresa el valor y el programa arroja el resultado directamente antes de agregar siguiente valor 
  x = float(input( "Introduce un numero al que le quieras hallar la raiz cuadrada: "))
  raiz_cuadrada = math.sqrt(x)
  print("La raíz cuadrada de  " + str(x) + " es " + str(math.sqrt(x)))

  y = float(input("Ingrese el número del cual quiere conocer su coseno: "))
  coseno_numero = math.cos(y)
  print("El coseno de  " + str(y) + " es " + str(math.cos(y)))

  z = float(input("Ingrese el número del cual quiere conocer su tangente: ") )
  tangente_numero = math.tan(z)
  print("La tangente de  " + str(z) + " es " + str(math.tan(z)))

  l = int(input("Ingrese los grados que quiere convertir en radianes: "))
  radianes_grados = math.radians(l)
  print("Los grados " + str(l) + " son equivalentes a " + str(math.radians(l)) + " radianes")
  
  s = float(input("Ingrese el número del cual quiere conocer su valor absoluto: "))
  valor_absoluto_numero = math.fabs(s)
  print("El valor abdsoluto de " + str(s) + " es " + str(math.fabs(s)))
```

