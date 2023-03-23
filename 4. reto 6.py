def d(P:int, M:int, H:int, B:float) -> float:
    d = (P*300) + (M*3300) + (H*350) - B
    return d

if __name__ == '__main__':
    P = int(input("Ingresar el numero de panes a comprar: "))
    M = int(input("Ingresar el numero de bolsas de leche a comprar : "))
    H = int(input("Ingresar el numero de huevos a comprar: "))
    B = float(input("Ingresar la cantidad de dinero: "))
    cambio = d(P, M, H, B)
    print("Las vueltas que me deben dar o el dinero que me falta es: " + str(d))