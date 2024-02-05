import random

def spostamentoCasuale():
    return random.choice([-1, 1])

def calcolaSomma(spostamentiCasuali):
    somma = 0
    for numero in spostamentiCasuali:
        somma += numero
    return somma

def main():
    listaSpostamenti = [spostamentoCasuale() for _ in range (0, 43200)]

    somma = calcolaSomma(listaSpostamenti)

    print(somma)
if __name__ == "__main__":
    main()