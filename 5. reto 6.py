def calculo_del_valor_del_prestamo (c:int, i:int, n:int) -> int:
 
  valor_prestamo= c*(1+(i/100))**n
  return valor_prestamo
if __name__ == "__main__":
      c= int(input("Ingrese el valor del prestamo en pesos:"))
      i = int(input("Ingrese el porcentaje de interes:"))
      n  = int(input("Ingrese la cantidad de meses :"))

      valor_del_prestamo = calculo_del_valor_del_prestamo(c, i, n)

      print("El valor del pretamo es " + str(valor_del_prestamo))
      