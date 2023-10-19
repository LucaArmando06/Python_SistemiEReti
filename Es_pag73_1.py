def main():
    n = int(input("inserisci un numero: "))
    div = 3
    
    if n % div == 0:
        print(f"Il numero {n} è divisibile per 3")
    else:
        print(f"Il numero {n} non è divisibile per 3")

if __name__ == "__main__":
   main()

 