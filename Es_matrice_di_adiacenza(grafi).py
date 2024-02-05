import networkx as nx
import matplotlib.pyplot as plt

def rappresentaAdiacenze(collegamenti):
    G = nx.Graph(collegamenti)
    pos = nx.spring_layout(G)  # Layout del grafo

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black', font_family='sans-serif')

    plt.title("Rappresentazione grafica delle adiacenze")
    plt.show()

def stampa(matrice, separatore):
    for riga in matrice:
        riga_str = [str(x) for x in riga] #coverto la lista di numeri in lista di stringhe
        print(separatore.join(riga_str)) #unisco gli elemnti della lista separati dal carattere spazio


def trasformaMatrice(matrice):
    dizionario = {chiave: [] for chiave in range(len(matrice))}
    v = 0
    for riga in matrice:
        n = 0
        for elemento in riga:
            if elemento == 1:
                dizionario[v].append(n) #append per aggiungere il numero alla lista
            n += 1
        v += 1
    return dizionario


def main():
    collegamenti = {0: [2, 3], 1: [2, 4], 2: [0, 1, 3], 3: [0, 2, 4], 4: [1, 3]}
    
    n = len(collegamenti)

    matrice = [[0] * n for _ in range(n)]

    for vertice in collegamenti:
        for punto in collegamenti[vertice]:
            matrice[vertice][punto] = 1

    print(collegamenti)

    stampa(matrice, " ")
        
    dizionario = trasformaMatrice(matrice)
    print(dizionario)

    rappresentaAdiacenze(collegamenti)

if __name__ == "__main__":
    main()
