def main():
    n = int(input("inserisci la subnetMask in notazione CIDR: "))
    subnetmask_bin = "1"*n + "0"*(32-n)
    print(subnetmask_bin)
    gruppo1 = subnetmask_bin[0:8]
    gruppo2 = subnetmask_bin[8:16]
    gruppo3 = subnetmask_bin[16:24]
    gruppo4 = subnetmask_bin[24:32]
    gruppo1 = int(gruppo1, 2)
    gruppo2 = int(gruppo2, 2)
    gruppo3 = int(gruppo3, 2)
    gruppo4 = int(gruppo4, 2)
    subnetmask_dec = f"{gruppo1}.{gruppo2}.{gruppo3}.{gruppo4}"
    print(subnetmask_dec)
if __name__ == "__main__":
    main()