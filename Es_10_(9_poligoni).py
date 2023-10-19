def main():
    import turtle

    finestra = turtle.Screen()
    finestra.bgcolor("white")

    lato = 20
    spazio = 100

    for i in range(9):
        alice = turtle.Turtle()
        alice.penup()
        alice.goto((i % 3) * spazio, -(i // 3) * spazio)
        alice.pendown()

        angolo = 360 / i + 3

        for _ in range(i + 3):
            alice.forward(lato)
            alice.right(angolo)

    finestra.mainloop()
    
if __name__ == "__main__":
    main()
