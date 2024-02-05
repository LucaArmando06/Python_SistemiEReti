import turtle
def disegnaQuadrato(alice, lung, lati):
    for _ in range(0, lati):
        alice.forward(lung)
        alice.left(90)
def disegnaRiga(alice, lung, lati):
    for _ in range(0, 4):
        disegnaQuadrato(alice, lung, lati)
        alice.forward(100)
def main():
    lung = 100
    lati = 4
    finestra = turtle.Screen()
    alice = turtle.Turtle()
    alice.speed(10)
    disegnaRiga(alice, lung, lati)
    alice.right(180)
    disegnaRiga(alice, lung, lati)
    alice.left(90)
    alice.forward(200)
    alice.left(90)
    disegnaRiga(alice, lung, lati)
    alice.right(180)
    disegnaRiga(alice, lung, lati)
    finestra.mainloop()

    alice.penup()
    for cont in range (LATI)
        for i in range (LATI)


if __name__ == "__main__":
    main()
