def main():
    n = int(input("inserisci un numero: "))

    if n % 2 == 0:
        print(f"Il numero {n} è divisibile per 2")
    elif n % 3 == 0:
         print(f"Il numero {n} è divisibile per 3")
    elif n % 5 == 0:
        print(f"Il numero {n} è divisibile per 5")
    else: 
        print(f"Il numero {n} non è divisibile per 2, 3 o 5")

if __name__ == "__main__":
   main()

 