
def kilogramos_de_carne_de_aves(N:int, M:int, K:int) -> int:
    return N*6 + M*7 + K*1

if __name__ == '__main__':
    
    N = int(input("Ingresar el numero de gallinas: "))
    M = int(input("Ingresar el numero de gallos: "))
    K = int(input("Ingresar el numero de pollitos: "))
    
    
    peso_de_la_carne = kilogramos_de_carne_de_aves (N, M, K)
    print("El peso de la carne de las aves es de  " + str(peso_de_la_carne) + " kilogramos ")
    