import turtle
LUNG = 100

class Barcode():
    def __init__(self, codice):
        self.codice = codice

    def disegnaCodice(self):
        for carattere in self.codice:
            carattereAscii = ord(carattere) 
            
        carattereBin = format(int(carattereAscii), '08b')

        print(carattereBin)        

        for numero in carattereBin:
            if numero == 1:
                turtle.color("black")
                turtle.left(90)
                turtle.forward(LUNG)
                turtle.right(90)           
                turtle.forward(1)
                turtle.right(90) 
                turtle.forward(LUNG)
                turtle.left(90)           
                turtle.forward(1)
                turtle.left(90) 
                turtle.forward(LUNG)
                turtle.right(90)           
                turtle.forward(1)
                turtle.right(90) 
                turtle.forward(LUNG)
                turtle.left(90)
                turtle.forward(2)
                turtle.left(90)
            else:
                turtle.color("white")
                turtle.left(90)
                turtle.forward(LUNG)
                turtle.right(90)           
                turtle.forward(1)
                turtle.right(90) 
                turtle.forward(LUNG)
                turtle.left(90)           
                turtle.forward(1)
                turtle.left(90) 
                turtle.forward(LUNG)
                turtle.right(90)           
                turtle.forward(1)
                turtle.right(90) 
                turtle.forward(LUNG)
                turtle.left(90)
                turtle.forward(2)
                turtle.left(90)

        
def main():
    #codice = str("Inserisci un codice alfanumerico: ")

    codice = "ciao1234"
    finestra = turtle.Screen() 

    codiceBarre = Barcode(codice)
    codiceBarre.disegnaCodice()

    finestra.mainloop()
    
if __name__ == "__main__":
    main()