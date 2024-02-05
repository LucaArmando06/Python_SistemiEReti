class Quadrato():
    def __init__(self, lato):
        self.lato = lato

    def calcolaArea(self):
        return self.lato * self.lato

    def calcolaPerimetro(self):
        return 4 * self.lato
 
    def verificaPunto(self, x, y):
        if x > 0 and x < self.lato and y > 0 and y < self.lato:
            return False
        else:
            return True

def main():
    quadrato = Quadrato(5)

    print(f"Area del quadrato: {quadrato.calcolaArea()}")
    print(f"Perimetro del quadrato: {quadrato.calcolaPerimetro()}")

    if quadrato.verificaPunto(2, 2):
        print(f"Il punto è esterno al quadrato.")
    else:
        print(f"Il punto è interno al quadrato.")

if __name__ == "__main__":
    main()