def main():
    import turtle

    finestra = turtle.Screen()
    finestra.bgcolor("white")

    alice = turtle.Turtle()

    n_punte = 6 
    lunghezza = 30

    if n_punte < 5:
        angolo_esterno = 360 / n_punte
        angolo_interno = 180 - angolo_esterno
        for _ in range(n_punte):
            alice.forward(lunghezza)
            alice.right(angolo_interno * 2)  
            alice.forward(lunghezza)
            alice.left(angolo_esterno)

    finestra.mainloop()

if __name__ == "__main__":
    main()