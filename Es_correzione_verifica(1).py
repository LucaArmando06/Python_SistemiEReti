class Testo():
    def __init__(self, testo):
        self.testo = testo
        self.lista = self.testo.split(" ")

    def calcolaCaratteri(self):
        return len(self.testo)
    
    def lista_parole(self):
        return self.testo.split(" ")
    
    def lunghezzaParole(self):
        return [len(parola) for parola in self.lista]
    
    def ricerca(self, parola):
        return parola in self.lista
    
    def salva(self, nomefile):
        with open(nomefile, "w") as file:
            file.write(self.testo)

    def frequenze_parole(self):
        frequenze = {}
        for parola in self.lista: 
            if parola in frequenze: 
                frequenze[parola] += 1
            else: 
                frequenze[parola] = 1
        return frequenze


def main():
    prova = "ciao come stai?"
    t = Testo(prova)
    print(t.calcolaCaratteri())
    print(t.lista_parole())
    print(t.lunghezzaParole())
    print(t.ricerca("mario"))
    print(t.ricerca("ciao"))
    print(t.frequenze_parole())
if __name__ == "__main__":
    main()