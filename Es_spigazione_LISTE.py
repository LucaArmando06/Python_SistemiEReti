#LE LISTE 
def print_list(l):
    print("la lista è: ")
    for elemento in l:
        print(elemento, end = " ")
    print("\n")

def main():
    #l = [1, 2, 3, 4, "c", 3.14, "python"]
    #r = [10, 11, 12]
    #print_list(l + r) #concatena l e r 
    #print_list(r*3) #concatena tre volte r su se stessa 

    #vogliamo permettere all'utente di caricare una lista
    lista = []
    num = 1
    while num > 0:
        num = int(input("Inserire un numero: (-1 per interrompere): "))
        if(num > 0):
            lista.append(num) #append per aggiungere un numero alla lista
    
    print_list(lista)

if __name__ == "__main__":
   main()