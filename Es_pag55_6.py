def main():
    stringa = "ciao"

    for cont in stringa:
        if (stringa.index(cont) % 2 != 0):
            print(cont)

if __name__ == "__main__":
    main() 