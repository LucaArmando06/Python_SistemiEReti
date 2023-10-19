def print_list(l):
    print("la lista è: ")
    for elemento in l:
        print(elemento, end = " ")
    print("\n")

def main():
    lista_voti = [6.5, 8, 10, 5, 4.5, 7, 8,5]

    print(f"lista senza primo e ultimo voto: {lista_voti[1:-1]}")

    lista_voti.remove(3)  # Rimuove il voto alla posizione 3
    lista_voti.append(3, '9')  # Inserisce il voto '9' alla posizione 3
    print_list(lista_voti)

    print(f"primi tre voti della lista: {lista_voti[0:4]}")

if __name__ == "__main__": 
    main()