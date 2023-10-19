#SLICING DI STRINGHE 
s = "ciao come stai?"  
#stringa ciao composta da 0 1 2 3  in python anche -4 -3 -2 -1 
print(f"il primo carattere è {s[0]}")
print(f"l'ultimo carattere è {s[-1]}") #funziona sempre anche se non so quanto è lunga la stringa 
print(f"il penultimo carattere è {s[-2]}") #se mi interessano i primi caratteri uso indicizzazione 
                                            #normale se mi servono gli ultimi uso quella negativa 

print(s[3:7]) #voglio stampare dal carattere 3 escluso al carattere 7 escluso
print(f"tutta la stringa esclusi il primo e l'ultimo carattere: {s[1:-1]}") #da secondo a penultimo 
print(f"tutta la stringa escluso il primo carattere: {s[1:]}") #da secondo a ultimo
print(f"tutta la stringa escluso l'ultimo carattere: {s[:-1]}") #tutto tranne ultimo
print(s[::-1]) #stampa la stringa invertita dall'ultimo al primo