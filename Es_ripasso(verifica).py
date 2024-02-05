lettere = "abcdefghilmnopqrstuvz ?!"
N = len(lettere)
lettere2numeri = {}
numeri2lettere = {}

#esempio senza enumerate
#contatore = 0
#for lettera in lettere: 
 #   lettere2numeri[lettera] = contatore
  #  contatore += 1

#print(lettere2numeri)

#exit()


for posizione, lettera in enumerate (lettere):
    lettere2numeri[lettera] = posizione
    numeri2lettere[posizione] = lettera

testo_chiaro = "ciao come stai?"
chiave = "it isdel pozz overv eksd vcerw qmgltr"

testo_criptato = ""
testo_decriptato = ""

for lettera_testo, lettera_chiave in zip(testo_chiaro, chiave): #ciclo con zip(cicla in parallelo 2 due stringhe) ongi lettera della parola che voglio codificare 
    numero = (lettere2numeri[lettera_testo] + lettere2numeri[lettera_chiave]) % N
    testo_criptato = testo_criptato + numeri2lettere[numero]

print(f"il testo '{testo_chiaro}' diventa '{testo_criptato}'.")

for lettera_testo, lettera_chiave in zip(testo_chiaro, chiave): #ciclo con zip(cicla in parallelo 2 due stringhe) ongi lettera della parola che voglio codificare 
    numero = (lettere2numeri[lettera_testo] - lettere2numeri[lettera_chiave]) % N
    testo_decriptato = testo_decriptato + numeri2lettere[numero]

print(f"il testo '{testo_criptato}' diventa '{testo_decriptato}'.")

#da ripassare join, split, classi, dizionari, scrittura e lettura file