def main():
    n1 = float (input("inserisci il primo numero: "))
    n2 = float (input("inserisci il secondo numero: "))

    if n1 < n2: 
        n1, n2 = n2, n1

    print(f"{n1} {n2}")

if __name__ == "__main__":
   main()

 