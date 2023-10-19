def main():
    import turtle
    
    n = int (input("inserisci il numero dei lati: "))
    lato = int (input("inserisci la lunghezza dei lati: "))
    finestra = turtle.Screen()
    alice = turtle.Turtle()

    alice.begin_fill()
    for i in range (0, n): 
        alice.color('green')
        alice.forward(lato)
        alice.left(360/n)
    alice.end_fill()

    finestra.mainloop()  

if __name__ == "__main__":
   main()