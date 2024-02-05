class Quadrato():
    def __init__(self, lato): #sempre così il costruttore in tutte le classi (non come in java che è il nome è quello dell classe)
        self.lato = lato

    def calcolaArea(self): #a tutti i metodi delle classi gli devo passare self 
        return self.lato**2
    
    def stampaLato(self): #con self mi riferisco all'attributo (come this in java)
        print(f"Il lato è {self.lato}") 
    
def main():
    q = Quadrato(4) #chiamo il nome della classe non del suo costruttore
    print(f"L'area del quadrato è: {q.calcolaArea()}") #nella chiamata non devo passare il self
    q.stampaLato()
    q.lato = 5  #posso cambiare il valore dell'attributo lato perchè è tutto public 
    print(f"L'area del quadrato è: {q.calcolaArea()}")
    q.stampaLato()

if __name__ == "__main__":
    main()