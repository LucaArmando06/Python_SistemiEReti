def cercaNome(rubrica, ricercato): #(chiave numero) cerca il nome che gli viene inserito 
    for numTel in rubrica:
        if rubrica[numTel] == ricercato:
            return numTel
    return None

def cercaNumTel(rubrica, numTelDaTrovare): #(chive numero) cerca il numero che gli viene inserito
    if numTelDaTrovare in rubrica:
        return rubrica[numTelDaTrovare]
    else:
        return None
    
def main():
    file = open("Rubrica.txt", "r")
    righe = file.readlines()
    file.close()
    rubrica = {}

    for riga in righe:
        campi = riga.split(",") #campi è una lista
        numeroTelefonico = int(campi[1].replace("\n", "")) #sostituisco il carattere \n con sringa vuota 
        nome = campi[0]
        rubrica[numeroTelefonico] = nome #la chiave è il numero telefonico

    print(rubrica)

    ricercato = input("inserire nome o numero di telefono da ricercare: ")
    
    risultato = cercaNome(rubrica, ricercato)
    print(f"Numero di {ricercato}: {risultato}")

    numDaTrovare = int(input("inserire nome o numero di telefono da ricercare: "))
    risultato2 = cercaNumTel(rubrica, numDaTrovare)
    print(f"Il numero {numDaTrovare} è di: {risultato2}")


if __name__ == "__main__":
    main()