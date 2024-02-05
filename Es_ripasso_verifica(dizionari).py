dizionario = {"a": "albero", "b": "brutto", "c": "casa"}

print(dizionario["b"])
dizionario["d"] = "dado" #aggiungo elemento

dizionario["a"] = "alto" #sovrascrive 
print(dizionario)

for chiave in dizionario: #ciclo le chiavi
    print(f"la chiave {chiave} ha valore: {dizionario[chiave]}")

if "a" in dizionario: #controllo se c'è la chiave nel dizionario
    print("a è presente nel dizinario")