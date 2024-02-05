import turtle
import random
MOVIMENTO = 10

def nord(bob):
    bob.seth(90)
    bob.forward(MOVIMENTO)

def sud(bob):
    bob.seth(270)
    bob.forward(MOVIMENTO)

def est(bob):
    bob.seth(0)
    bob.forward(MOVIMENTO)

def ovest(bob):
    bob.seth(180)
    bob.forward(MOVIMENTO)

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    finestra = turtle.Screen() 
    bob = turtle.Turtle()

    spostamenti = {"n": nord, "s": sud, "e": est, "o": ovest}
    sposta = ["n", "s", "e", "o"]
    percorso = {0: Punto(0,0)} #dizionario che contiene la posizione del punto nei vari minuti

    for minuto in range (1, 60): #simulare movimenti casuali e controllo se non è gia stato in quel punto
        movimento = random.choice(sposta)
        spostamenti[movimento](bob)
        percorso[minuto] = Punto(bob.xcor(), bob.ycor())


    #manca BONUS


    #scrivere su file del percorso COLONNE: minuto, x, y
    with open ("perscorso.csv", "w") as file: 
        #ciclo sul dizionario percorso per sciverlo nel file
        for minuto in percorso:
            posx = int(percorso[minuto].x)
            posy = int(percorso[minuto].y)
            file.write(f"{minuto},{posx},{posy}\n") 

if __name__ == "__main__":
    main()