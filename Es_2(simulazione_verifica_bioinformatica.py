def leggiFile():
    file = open("covid-19_gen1.txt", "r")
    righeFile = file.readlines()
    file.close()
    genoma = ""

    for riga in righeFile: 
       riga = riga[:-1] 
       genoma = genoma + riga

    return genoma

def leggiFile2():
    genoma = ""
    
    with open("covid-19_gen1.txt", "r") as file:
        righeFile = file.readlines()

    for riga in righeFile: 
       riga = riga[:-1] 
       genoma = genoma + riga

    return genoma

def calcolaNucleotidi1(genoma):
    numA, numT, numG, numC = 0, 0, 0, 0

    for lettera in genoma:
        if lettera == 'A':
            numA = numA + 1
        elif lettera == 'C':
            numC = numC + 1
        elif lettera == 'G':
            numG = numG + 1
        elif lettera == 'T':
            numT = numT + 1
    return numA, numC, numG, numT

def calcolaNucleotidi2(genoma):
    dizNucleotidi = {"A": 0, "C": 0, "G": 0, "T": 0}
    for char in genoma:
        dizNucleotidi[char] += 1
    return dizNucleotidi

def calcolaNucleotidi3(genoma, nucleotide):
    return len([x for x in genoma if x == nucleotide])

def cercaProteinaSpike(genoma):
    proteinaSpike = "ATGTTTGTTTTT"
    for i, _ in enumerate(genoma[:-12]):
        if genoma[i:i+len(proteinaSpike)] == proteinaSpike:
            return i
    return -1

def main():
    genoma = leggiFile()
    
    print(genoma)
    
    numA, numC, numG, numT = calcolaNucleotidi1(genoma)
    
    print(f"A: {numA}, C: {numC}, G: {numG}, T: {numT}")

    pos = cercaProteinaSpike(genoma)
    print(pos)
    #print(genoma.find("ATGTTTGTTTTT"))

if __name__ == "__main__":  
    main()