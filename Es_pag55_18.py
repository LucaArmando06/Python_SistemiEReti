def calcola_quadrato(num):
    return num*num

def main():
    num1 = int(input("inserire un numero: "))
    num2 = int(input("inserire un secondo numero: "))
    lista = [calcola_quadrato(num1) + calcola_quadrato(num2), calcola_quadrato(num1 + num2), calcola_quadrato(num1) - calcola_quadrato(num2), calcola_quadrato(num1 - num2)]
    print(lista)

if __name__ == "__main__":
    main()