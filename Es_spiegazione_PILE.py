def push(pila, elemento):
    pila.append(elemento) #per fare push si usa append

def pop(pila):
    x = pila.pop()
    return x

def main():
    pila = [1,2,3,4]
    push(pila, 10)
    print(pila)
    x = pop(pila)
    print(x, pila)

if __name__ == "__main__":
    main()