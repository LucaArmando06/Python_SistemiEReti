def main():
    nome = input ("Come ti chiami? ") #per fare inserire il nome metto input
    anni = int(input("Quanti anni hai? "))
    anno_corrente = int (input("In quale anno siamo?"))

    print(f"Il tuo nome è {nome} e hai {anni} anni") #va a capo da sola 
    print(f"Sei nato nel {anno_corrente - anni}")

    # print(type(anni)) #type per sapere il tipo di qualunque variabile 

if __name__ == "__main__":
   main()   