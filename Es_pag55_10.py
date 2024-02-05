def print_list(l):
    print("la lista è: ")
    for elemento in l:
        print(elemento, end = " ")
    print("\n")

def main():
    lista_voti = []
    voto = 1    
    k = 0

    while True:
        voto = int(input("Inserisci un voto (-1 per interrompere): "))
        if (voto < 0 and k >= 6):
            break
        lista_voti.append(voto)
        k += 1

    print(f"lista senza primo e ultimo voto: {lista_voti[1:-1]}")
    lista_voti[3] = 10  
     
    print_list(lista_voti)
    print(f"primi tre voti della lista: {lista_voti[0:4]}")

if __name__ == "__main__": 
    main()