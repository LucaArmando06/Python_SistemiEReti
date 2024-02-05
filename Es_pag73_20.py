def main():
    max = 10
    tavola_pitagorica = [[k * i for i in range (1, max + 1)] for k in range (1, max + 1)]
    for k ,tabellina in enumerate(tavola_pitagorica):
        #tabellina = lista 
        #tavola_pitagorica = lista di liste 
        #enumerate funzione che numera le liste e ritorna indice e elemento 
        print (f"(tabellina del: {k + 1}: {tabellina})")

    file = open("Data.txt", "w")

    for tabellina in tavola_pitagorica:
        file.write(f"{tabellina}\n")

    file.close()
if __name__ == "__main__":
    main()  