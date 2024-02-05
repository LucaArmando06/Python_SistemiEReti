def main():
    lista = ["ciao"]
    lista_senza_vocali = ''.join([carattere for carattere in lista if carattere.lower() not in 'aeiou'])
    print("Stringa originale:", lista)
    print("Stringa senza vocali:", lista_senza_vocali)
if __name__ == "__main__":
    main()