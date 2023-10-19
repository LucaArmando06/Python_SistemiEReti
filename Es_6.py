def main():
    lista = [4, 100, 3, 5, "ciao", print] #lista

    #ciclo for C-style
    for i in range (0, len(lista)): #len da lunghezza della lista
        print(f"L'elemento {i}-esimo della lista è  {lista[i]}")

    #ciclo for Pyhton-styile
    for elemento in lista:
        print(f"Elemento: {elemento}")

if __name__ == "__main__":
   main()

 