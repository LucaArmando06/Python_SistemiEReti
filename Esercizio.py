def cercaNome(rubrica, nomeDaCercare):
    for numTel in rubrica:
        if rubrica[numTel] == nomeDaCercare:
            return numTel
    return None
        
def cercaNumero(rubrica, numDaCercare):
    for numTel in rubrica:
        if numTel == numDaCercare:
            return rubrica[numTel]
    return None

def main():
    file = open("Rubrica.txt", "r")
    righe = file.readlines()
    file.close()

    rubrica = {}

    for riga in righe:
        numeroTelefono = int(riga.split(",")[1].replace("\n", ""))
        persona = riga.split(",")[0]
        rubrica[numeroTelefono] = persona

    print(rubrica)

    nomeDaCercare = input("inserisci un nome da cercare: ")
    numeroTrovato = cercaNome(rubrica, nomeDaCercare)
    print(f"Numero di {nomeDaCercare}: {numeroTrovato}")

    numDaTrovare = int(input("inserire numero di telefono da ricercare: "))
    nomeTrovato = cercaNumero(rubrica, numDaTrovare)
    print(f"Il numero {numDaTrovare} è di: {nomeTrovato}")

    nuovo = input(f"inserisci il nome e il numero da inserire (nome, numero): ")
    with open("Rubrica.txt", "a") as file:
        lista = nuovo.split(", ") #divido la stringa che mi inserisce su stringa e divide in lista di diversi elementi
        nome = ", ".join(lista) #unisco la stringa separata  unisce lista in una stringa separata da quello che voglio
        file.write("\n" + nome)


if __name__ == "__main__":
    main()