def somma(a, b):
    return a + b 

def prodotto(a, b):
    return a * b

def divisione(a, b):
    return a / b

def sottrazione(a, b):
    return a - b

def main():
    dizionario = {"+": somma, "*": prodotto, "/": divisione, "-": sottrazione} #nel dizionario ad ogni chiave assegno una funzione che fa se c'è quella chiave
    operazione = input("Scrivi + per somma, * per prodotto, / per divisione, - per sottrazione: ")
    if operazione in dizionario:
        a = float(input("Scrivi il primo numero: "))
        b = float(input("Scrivi il secondo numero: "))
        print(dizionario[operazione](a, b))  #dizionario[operazione] è di tipo funzione quindi gli passo i parametri
    else:
        print("Errore")
if __name__ == "__main__":
    main()