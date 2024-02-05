def calcolaSubnetMask(indirizzo_ip, n):
    sub_bin = "1" * n + "0" * (32 - n)
    gruppo1 = int(sub_bin[0:8], 2)
    gruppo2 = int(sub_bin[8:16], 2)
    gruppo3 = int(sub_bin[16:24], 2)
    gruppo4 = int(sub_bin[24:32], 2) 
    sub_dec = f"{gruppo1}.{gruppo2}.{gruppo3}.{gruppo4}"
    return sub_dec

def main():
    indirizzi_ip = ["192.168.222.0/27", "192.168.100.0/24", "192.168.200.0/28", "192.168.50.0/22"]

    file = open("mask.txt", "w")

    for indirizzo in indirizzi_ip:
        n = int(indirizzo.split("/")[1]) #split ritorna una lista di due stringhe quindi devo fare il casting e il [1]
        subnet_mask = calcolaSubnetMask(indirizzo, n)
        file.write(f"{indirizzo} - {subnet_mask}\n")

    file.close()

if __name__ == "__main__":
    main()