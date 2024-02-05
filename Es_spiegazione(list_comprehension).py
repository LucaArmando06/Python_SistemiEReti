#list comprehension
#lista con i primi 5 quadrati perfetti
import random
quadrati = [i*i for i in range(1,6)]
numeri_interi = [i for i in range (1,11)] #mette in una lista i numeri interi da 1 a 10 

stringhe = ["computer", "celulare", "laptop"]

stringhe_c = [parola for parola in stringhe if parola[0] == "c"] #mette solo le parole che iniziano per C in stringhe_c
print(stringhe_c)

voti = [random.randint(2,10) for _ in range (10)] #mette nella stringa random 10 numeri interi a caso ( _ per volore di una variabile che poi non uso)
print(voti)
 
voti_insuf = [voto for voto in voti if voto < 6]
print(voti_insuf)