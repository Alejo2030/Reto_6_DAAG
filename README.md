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


## Puntos del reto

1.Dado la figura de la imagen, desarrolle: 

[![reto-6.png](https://i.postimg.cc/4NL4z2dd/reto-6.png)](https://postimg.cc/cr3NWmfy)


### Una función matemática para calcular el volumen y el área superficial.

### Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.

### Revise como utilizar el valor de pi usando import math y math.pi 


```ruby
import math

def hallar_volumen_figura(r1:float,r2:float,h:float)-> float:
    hallar_volumen_figura = (r2**2*h*math.pi)/3 +(r1*3*4*math.pi)/3
    return hallar_volumen_figura 

def  hallar_area_de_la_figura(r1:float,r2:float,h:float) -> float:
    hallar_area_de_la_figura = (r1*2*4*math.pi)+(r2*math.pi)*(r2+(r2**2+h**2)**(1/2))
    return hallar_area_de_la_figura

if __name__ == "__main__":
  r1 = float(input("Ingrese el radio de la esfera que va a utilizar: "))
  r2 = float(input("Ingrese el radio del cono que va a utilizar: "))
  h = float(input("Ingrese la altura del cono que va a utilizar: "))

  vf =  hallar_volumen_figura(r1,r2,h)
  af=   hallar_area_de_la_figura(r1,r2,h) 
  print("El volumen de la figura es " + str(vf)) 
  print("El area de la figura es " + str(af))
  ```
  


