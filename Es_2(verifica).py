def main():
    for num in range (1, 999):
        n = str(num)
        n.split()
        somma = 0
        for cifra in n:
            somma = somma + int(cifra) * int(cifra) * int(cifra)
            if somma == n:
                print(n)

if __name__ == "__main__":
    main()