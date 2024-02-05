import turtle
PIXEL = 100

def nord():
    alice = turtle.Turtle()
    alice.seth(90)
    alice.forward(PIXEL)

def sud():
    alice = turtle.Turtle()
    alice.seth(270)
    alice.forward(PIXEL)

def est():
    alice = turtle.Turtle()
    alice.seth(0)
    alice.forward(PIXEL)

def ovest():
    alice = turtle.Turtle()
    alice.seth(180)
    alice.forward(PIXEL)

def main():
    dizionario = {"n": nord, "s": sud, "e": est, "o": ovest}
    movimento = input("Scrivi n per andare a nord, s per andare a sud, e per andare a est, o per andare a ovest: ")
    
    finestra = turtle.Screen() 
    
    if movimento in dizionario:
        dizionario[movimento]()
    
    else:
        print("Erorre")
        
if __name__ == "__main__":
    main()