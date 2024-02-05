#dizionario: collezione di coppie chiave:valore
#il dizionario non ha indici ma si indicizza per chiave

dizionario = {"nome": "Mario", "cognome": "Rossi"}  #liste con []    dizionari con {}
print(dizionario["nome"])

dizionario["data nascita"] = "01/01/1900" #aggiungo elemento con chiave "data nascita"
dizionario["anni"] = 123

dizionario["nome"] = "Luca" #sovrascrivo elemento in chiave "nome"
print(dizionario)

#MODO 1 per ciclare sui dizionari
for chiave in dizionario:
    print(f"Chiave: {chiave} - valore: {dizionario[chiave]}")

rubrica = {38189192: "Mario Rossi", 348039013: "Alice Verdi"}
print(rubrica)