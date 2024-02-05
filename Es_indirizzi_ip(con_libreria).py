import ipaddress

def main():
    indirizzoIP = input("Inserisci un indirizzo IP: ")
    subnetMask = input("Inserisci la subnet mask: ")
    ip = ipaddress.IPv4Address(indirizzoIP)
    indirizzo = indirizzoIP + subnetMask

    if ip.is_private:
        print(f"L'indirizzo {indirizzo} è privato.")
    else:
        print(f"L'indirizzo {indirizzo} non è privato.")

    if ip.is_loopback:
        print(f"L'indirizzo {indirizzo} è di loopback.")
    else:
        print(f"L'indirizzo {indirizzo} non è di loopback.")

    ipRete = ipaddress.IPv4Network(indirizzo, strict=False)
    if indirizzo == str(ipRete):
        print(f"è di rete perchè l'indirizzo {indirizzo}")
    else: 
        print(f"non è di rete l'indirizzo {indirizzo} ")

    print(f"indirizzo di rete: {ipRete}")
    hosts = list(ipRete.hosts())
    print(f"il primo ip utilizzabile è: {hosts[0]}")
    print(f"il primo ip utilizzabile è: {hosts[-1]}")

if __name__ == "__main__":
    main()
