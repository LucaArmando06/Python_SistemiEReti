def print_list(l):
    print("la lista è: ")
    for elemento in l:
        print(elemento, end = " ")
    print("\n")

def main():
    comandiPossibili = ['F', 'R', 'L']
    lista = []

    num = 1

    while num not in comandiPossibili:
        num = (input("Inserisci un comando (F, R, L -1 per interrompere): "))
        if(num != '0'):
            lista.append(num) 
                        
    print_list(lista)

    import turtle
    finestra = turtle.Screen()
    alice = turtle.Turtle()

    for comando in lista:
        if (comando == 'F'):
            alice.forward(100)
        elif (comando == 'R'):
            alice.right(90)
        elif (comando == 'L'):
            alice.left(90)
    
if __name__ == "__main__":
   main()