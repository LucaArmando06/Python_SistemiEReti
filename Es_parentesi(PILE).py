def push(pila, elemento):
    pila.append(elemento) #per fare push si usa append

def pop(pila):
    if len(pila) == 0:
        x = None
    else:
        x = pila.pop()
    return x

def main():
    parentesi_aperte = ["{", "[", "("]
    parentesi_chiuse = ["}", "]", ")"]
    dizionario = {"{" : "}", "[" : "]", "(" : ")"}
    stringa = "{1+[2+3]*5}"
    pila = []
    errore = False
    posErrore = None
    for posCarattere, carattere in enumerate(stringa) :
        if carattere in parentesi_aperte:
            push(pila, carattere) 
        if carattere in parentesi_chiuse: #carattere è una parentesi chiusa
            parentesi = pop(pila) #parentesi è una parentesi aperta
            if parentesi != None:
                if dizionario[parentesi] != carattere: 
                    errore = True
                    posErrore = posCarattere
            else:
                errore = True 
                posErrore = posCarattere       

    if errore or pila:
        print(f"Errore in posizione: {posErrore} ")
    else:
        print("Corretto!")

if __name__ == "__main__":
    main()