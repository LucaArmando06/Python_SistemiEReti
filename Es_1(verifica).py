class Testo():
    def __init__(self, testo):
        self.testo = testo

    def calcolaCaratteri(self):
        caratteri = 0 
        for carattere in self.testo:
            caratteri += 1
        return caratteri

    def paroleContenute(self):
        lista = self.testo.split(" ")
        return lista
    
    def lunghezzaParole(self):
        lista = self.testo.split(" ")
        listaLung = []
        for parola, num in enumerate (lista):
            listaLung[num] = len(str(parola))
        return listaLung

    def cercaParola(self, parolaDaCercare):
        lista = self.testo.split(" ")
        for parola in lista:
            if parola == parolaDaCercare:
                return True
            else:
                return False 
            
    def salvaSuFile(self):
        file = open("testoSalvato.txt", "w")
        file.write(self.testo)
        file.close()

def main():
    testo = "ciao come stai"

    n = Testo(testo).calcolaCaratteri()
    print(n)

    listaParole = Testo(testo).paroleContenute()
    print(listaParole)

    #listaLung = Testo(testo).lunghezzaParole()
    #print(listaLung)

    print(Testo(testo).cercaParola("ciao"))

    Testo(testo).salvaSuFile()

if __name__ == "__main__":
    main()
