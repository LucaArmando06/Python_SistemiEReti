import turtle

def disegnaPoligono(t, num, lato):
    #disegno poligono
    gradi = 360 / num
    t.begin_fill()#la turtle inizia il riempimento
    for i in range(0,num):
        t.forward(lato)
        t.left(gradi)
    t.end_fill()#la turtle termina il riempimento

def posizionaTurtle(t, num, lato, x, y):
    #posiziona la turtle prima di disegnare il poligono
    t.penup()#la turtle si muove senza disegnare
    if(num%3 == 0):
        x = -100 
        y = y + lato*4
    else:
        x = x + lato*4
    t.goto(x, y)#la turtle si posiziona in x y
    t.pendown()#la turtle si muove disegnando
    return x,y

def main():
    x= 0
    y= -100
    lung = int(input("inserire il numero del lato: "))
    finestra = turtle.Screen()
    tarta = turtle.Turtle()
    tarta.shape("turtle")
    tarta.color("red")#colore della linea
    tarta.speed("slow")#velocità della turtle

    for num in range(3,12):
        x, y=posizionaTurtle(tarta, num, lung, x, y)
        disegnaPoligono(tarta, num, lung)
        
    finestra.mainloop() #gestione finestra

if __name__ == "__main__":
    main()
