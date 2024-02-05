class Coda:
    def __init__(self):
        self.lista = [] #lista è la coda

    def is_empty(self):
        if(len(self.lista) == 0):
            return True
        else: 
            return False

    def enqueue(self, elemento):
        self.lista.append(elemento)
    
    def dequeue(self):
        if(self.is_empty()):
            print("Lista vuota impossibile rimuovere")
            return None #se è vuota ritorna None quindi niente 
        else:
            return self.lista.pop(0) #uso pop(0) per rimuovere il primo 
        
    def stampaCoda(self):
        print(self.lista)

def main():
    coda = Coda()
    coda.enqueue(4)
    coda.dequeue(5)
    coda.stampaCoda()
    print(f"elemento rimosso: {coda.dequeue()}")
    print(f"elemento rimosso: {coda.dequeue()}")
    print(f"elemento rimosso: {coda.dequeue()}")
    coda.dequeue(39)
    coda.stampaCoda()

if __name__ == "__main__":
    main()