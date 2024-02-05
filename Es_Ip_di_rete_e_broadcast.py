def conversioneDecimale(ip_binario):
    gruppi_decimali = []
    for i in range(0 ,32, 8):
        ottetto = ip_binario[i:i+8]
        gruppi_decimali.append(str(int(ottetto, 2)))
        return ".".join(gruppi_decimali)

def main():
    ip = input("Inserisci un indirizzo IP (es. 192.168.1.1): ")
    n = int(input("Inserisci la subnet mask in notazione CIDR: "))
    
    sub_bin = "1" * n + "0" * (32 - n)
    gruppo1 = int(sub_bin[0:8], 2)
    gruppo2 = int(sub_bin[8:16], 2)
    gruppo3 = int(sub_bin[16:24], 2)
    gruppo4 = int(sub_bin[24:32], 2) 
    sub_dec = f"{gruppo1}.{gruppo2}.{gruppo3}.{gruppo4}"

    ip_bin_gruppi = [format(int(x), '08b') for x in ip.split('.')]
    ip_bin = ''.join(ip_bin_gruppi)

    ip_bin_rete = ip_bin[0:n] + "0" * (32 - n)
    ip_bin_broadcast = ip_bin[0:n] + "0" * (32 - n)

    print(conversioneDecimale(ip_bin_rete))
    print(conversioneDecimale(ip_bin_broadcast))
if __name__ == "__main__":
    main()
