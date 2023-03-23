def calculo_contagiados_del_covid(C:int,D:int) -> int:
    numero_de_contagiados_por_covid = C*(D)**2
    return numero_de_contagiados_por_covid

if __name__ == "__main__":
  C= int(input("Ingrese el número de contagiados actuales: "))
  D  = int(input("Ingrese los  dias transcurridos: "))

  CA= calculo_contagiados_del_covid(C,D)

  print("El numero de contagiados despues de "+ str(D)+ " dias seran "+ str(CA))