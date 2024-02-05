def completa8bit(strbin):  #strbin perchè passo stringa binaria
    b = strbin[2:]
    l = len(b)
    return "0"*(8-1)+b

def main():
    addres = input("inserisci un IP addres: ")  
    groups = addres.split(".") #split ritorna liste con i gruppi quando separati da un punto
    groups = [bin(int(group)) for group in groups] #numero_binario = bin(numero_decimale)[2:]
    print(addres)
    print(groups)
    print(completa8bit(groups[3]))
    groups_strbin = [completa8bit(strbin) for strbin in groups]
    print(groups_strbin)
    print(".".join(groups_strbin))

if __name__ == "__main__":
    main()