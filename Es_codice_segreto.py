#classe testo che può contenetre sia un testo in chiaro sia un testo codificato
#testo(testo, chiave, booleano se chiaro o codificato)
#metodi: cifra(), decifra()
#2 dizionari: chiave lettera e valore numero scritto a mano quello inverso lo scriviamo 
 #con un for che capovolge quello di prima creando un for vuoto di appoggio

class Testo():
    def __init__(self, testo, chiave, cifrato):
        self.testo = testo.lower()
        self.chiave = chiave.lower()
        self.cifrato = cifrato

    def cifra(self, dizionario):
        if self.cifrato == False: 
            lista_chiave = [c for c in self.chiave] 
            cifra = []
            for indice,car in enumerate(self.testo): #enumerate perchè sia indice che carattere parte da 0
                cifra.append((dizionario[car] + dizionario[lista_chiave[indice]]) % 21)
            self.cifrato = True
            print(",".join(str(c) for c in cifra)) #la virgola per separare i numeri
        else: 
            print("la stringa è gia cifrata")

    def decifra(self, dizionario, diz_num):
        if self.cifrato == True: 
            lista_chiave = [c for c in self.chiave] 
            cifra = []
            for indice,car in enumerate(self.testo): #enumerate perchè sia indice che carattere parte da 0
                cifra.append((dizionario[car] + dizionario[lista_chiave[indice]]) % 21)
            self.cifrato = True
            print(",".join(str(c) for c in cifra)) #la virgola per separare i numeri
        else: 
            print("la stringa è gia cifrata")



def main():
    dizionario = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "l": 9, "m": 10, "n": 11, "o": 12, "p": 13, "q": 14, "r": 15, "s": 16, "t": 17, "u": 18, "v":19, "z": 20}
    traduzione = {}
    
    for numero in dizionario:
        traduzione[dizionario[numero]] = numero
    
    print(dizionario)
    print(traduzione)
if __name__ == "__main__":
    main()