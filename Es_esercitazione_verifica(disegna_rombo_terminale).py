def main():
    n = int(input("inserisci un numero dispari: "))

    while n % 2 == 0:
        n = int(input("inserisci un numero dispari: "))

    sposta = n // 2  # // per avere solo la parte intera 
    
    asterischi = 1

    for i in range(sposta + 1):
        spazi_vuoti = sposta - i
        print(" " * spazi_vuoti + "*" * asterischi)
        asterischi += 2

    asterischi = n - 2

    for i in range(sposta):
        spazi_vuoti = i + 1
        print(" " * spazi_vuoti + "*" * asterischi)
        asterischi -= 2

if __name__ == "__main__":
    main()
