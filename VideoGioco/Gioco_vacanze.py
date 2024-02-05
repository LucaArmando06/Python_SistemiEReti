import pygame
import sys
import random

#inizializzazione di Pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH, HEIGHT = 1100, 700

#crea la finestra di gioco
finestra = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Ninja")


class Frutta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #devo metterlo perchè richiama il meteodo __init__ della classe madre di pygame.sprite.Sprite

        #lista di path delle immagini di diversi frutti
        immagini_frutta = ["immagini/anguria_chiusa.png", "immagini/mela_chiusa.png", "immagini/pera_chiusa.png", "immagini/banana_chiusa.png", "immagini/arancia_chiusa.png"]

        #sceglie casualmente un path di un immagine dalla lista
        self.path_immagine = random.choice(immagini_frutta)
        self.image = pygame.image.load(self.path_immagine)
        
        #dimensione delle immagini
        larghezza = 70 
        altezza = 80
        self.image = pygame.transform.scale(self.image, (larghezza, altezza))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = HEIGHT #parte dal basso

        self.direzione_y = 1  #1 indica che sta salendo, -1 indica che sta scendendo serve per invertire le direzione 
        self.direzione_x = random.choice([-1, 1])  #direzione orizzontale casuale -1 sinistra, 1 destra

    #funzione per gestire il movimento della frutta
    def update(self):
        self.rect.y -= 7 * self.direzione_y  #moltiplica la velocita per la direzione verticale
        self.rect.x += 5 * self.direzione_x  #moltiplica la velocita per la direzione orizzontale

        if self.rect.y < 100:
            self.direzione_y = -1 #quando tocca il limite in alto inverte la direzione per riscendere 

        if self.rect.y > HEIGHT:
            self.kill() #se dopo essere salita non viene colpita riscende e viene eliminata

        if self.rect.x < 0: 
            self.direzione_x = 1 #quando tocca i lati inverte la direzione per tornare verso il centro

        if self.rect.x > WIDTH:
            self.direzione_x = -1

class Bomba(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("immagini/bomba.png")

        larghezza = 70 
        altezza = 80
        self.image = pygame.transform.scale(self.image, (larghezza, altezza))
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = HEIGHT  #parte dal basso

        self.direzione_y = 1  #1 indica che sta salendo, -1 indica che sta scendendo serve per invertire le direzione 
        self.direzione_x = random.choice([-1, 1])  #direzione orizzontale casuale

    def update(self):
        self.rect.y -= 7 * self.direzione_y  #moltiplica la velocita per la direzione verticale
        self.rect.x += 5 * self.direzione_x  #moltiplica la velocita per la direzione orizzontale

        if self.rect.y < 100:
            self.direzione_y = -1 #quando tocca il limite in alto inverte la direzione per riscendere 

        if self.rect.y > HEIGHT:
            self.kill() #se dopo essere salita non viene colpita riscende e viene eliminata

        if self.rect.x < 0: 
            self.direzione_x = 1

        if self.rect.x > WIDTH:
            self.direzione_x = -1 #quando tocca i lati inverte la direzione per tornare verso il centro


class Spada(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("immagini/spada.png")

        larghezza = 60 
        altezza = 100
        self.image = pygame.transform.scale(self.image, (larghezza, altezza))
                
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


def schermataInizio():
    sfondo = pygame.image.load("immagini/sfondo_inizio.png")
    sfondo = pygame.transform.scale(sfondo, (WIDTH, HEIGHT))
    finestra.blit(sfondo, (0, 0))

    font = pygame.font.Font(None, 90)
    testo = font.render("Benvenuto a Fruit Ninja!", True, WHITE)
    finestra.blit(testo, (200, 220))

    font = pygame.font.Font(None, 50)
    testo_inizio = font.render("Premi un tasto per iniziare", True, BLACK)
    finestra.blit(testo_inizio, (320, 350))

    font = pygame.font.Font(None, 30)
    spiegazione = font.render("Per tagliare la frutta devi muoverti con il mouse e premere il tasto destro del mouse", True, WHITE)
    finestra.blit(spiegazione, (140, 550))

    font = pygame.font.Font(None, 30)
    spiegazione = font.render("LUCA ARMANDO", True, WHITE)
    finestra.blit(spiegazione, (460, 650))

    pygame.display.flip() #aggiorna schermata

    attesa_inizio = True
    while attesa_inizio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN: #se viene cliccato un qualsiasi tasto o mouse
                attesa_inizio = False

def disegnaSfondo():
    sfondo = pygame.image.load("immagini/sfondo.png")  
    sfondo = pygame.transform.scale(sfondo, (WIDTH, HEIGHT))
    finestra.blit(sfondo, (0, 0))

def generaFrutta(all_sprites, frutta_group):
    if random.randint(0, 100) < 3: #genera numeri casuali da 0 a 100 e genera frutta solo quando genera un numero minore di 2 cosi la probabilita non è altissima 
        nuova_frutta = Frutta()
        all_sprites.add(nuova_frutta)
        frutta_group.add(nuova_frutta)
        
def generaBombe(all_sprites, bomba_group):
    if random.randint(0, 100) < 1:
        nuova_bomba = Bomba()
        all_sprites.add(nuova_bomba)
        bomba_group.add(nuova_bomba)

def disegnaVite(bombe_colpite, MAX_COLPI_BOMBE):
    for i in range(bombe_colpite, MAX_COLPI_BOMBE):
        cuore = pygame.image.load("immagini/cuore.png")
        cuore = pygame.transform.scale(cuore, (50, 50))
        finestra.blit(cuore, (WIDTH - 80 - i * 70, 30))

def collisioniFrutta(punti, spada, frutta_group):
    collisioni_frutta = []
    if pygame.mouse.get_pressed()[0]: #devi premere il tasto destro (0)
        collisioni_frutta = pygame.sprite.spritecollide(spada, frutta_group, True)
    if collisioni_frutta:
        punti += 1 #se viene colpita aumenta il punteggio
    return punti

def collisioniBombe(spada, bomba_group, bombe_colpite): 
    collisioni_bombe = []
    if pygame.mouse.get_pressed()[0]:
        collisioni_bombe = pygame.sprite.spritecollide(spada, bomba_group, True)
        if collisioni_bombe:
            bombe_colpite += 1
    return bombe_colpite

def scrivePunteggio(punti):
        font = pygame.font.Font(None, 50)
        punteggio = font.render(f"Punteggio: {punti}", True, WHITE)
        finestra.blit(punteggio, (10, 10))

def fineGioco(punti): #funzione per ciò che viene fatto quando finisci una partita colpendo 3 bombe
    finestra.fill(BLACK) #pulisce la finestra e poi rimette l'immagine di sfondo con sopra l'immagine della scritta game over
    disegnaSfondo()
    scritta = pygame.image.load("immagini/game_over.png")  
    scritta = pygame.transform.scale(scritta, (600, 500))
    finestra.blit(scritta, (270, 110))
    pygame.display.flip() #aggiorna la finestra per mettere le immagini 
    pygame.time.wait(3000) #aspetta 3 secondi 

    finestra.fill(BLACK) #pulisce la finestra e poi scrive il punteggio finale
    
    disegnaSfondo()
                    
    font = pygame.font.Font(None, 60) 
    punteggio = font.render(f"Punteggio finale: {punti}", True, WHITE)
    finestra.blit(punteggio, (360, 250))
    pygame.display.flip()
    pygame.time.wait(2000)  

    #chiede all'utente se vuole iniziare una nuova partita o uscire
    domanda_font = pygame.font.Font(None, 50)
    domanda_text = domanda_font.render("Vuoi iniziare una nuova partita?", True, WHITE)
    finestra.blit(domanda_text, (300, 360))
    pygame.display.flip()
 
    bottone_si = pygame.image.load("immagini/bottone_si.png")
    bottone_no = pygame.image.load("immagini/bottone_no.png")
    bottone_si = pygame.transform.scale(bottone_si, (100, 100))
    bottone_no = pygame.transform.scale(bottone_no, (100, 100))
    finestra.blit(bottone_si, (400, 450))
    finestra.blit(bottone_no, (600, 450))
    pygame.display.flip() 

    risposta = None
    while risposta is None:
        for evento in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if evento.type == pygame.QUIT:
                risposta = False  #se l'utente chiude la finestra, esci dal gioco
            elif 400 <= mouse_x <= 500 and 450 <= mouse_y <= 550 and pygame.mouse.get_pressed()[0]: #per capire se  la posizione del mouse è tra le cordinate delle immagini dei pulsanti e clicchi il tasto destro
                risposta = True 
            elif 600 <= mouse_x <= 700 and 450 <= mouse_y <= 550 and pygame.mouse.get_pressed()[0]:
                risposta = False
                    
    if risposta:
        return True  #restituisce True se vuole iniziare una nuova partita
    else:
        return False  #restituisce False per chiudere il gioco


def main():
    #creazione delle sprite
    all_sprites = pygame.sprite.Group() #contiene tutte le sprite del gioco (spada, frutta e bombe)
    frutta_group = pygame.sprite.Group() #contiene solo la frutta per gestirla 
    bomba_group = pygame.sprite.Group()
    spada = Spada(0, 0)
    all_sprites.add(spada)

    clock = pygame.time.Clock()
    running = True
    punti = 0
    bombe_colpite = 0
    MAX_COLPI_BOMBE = 3

    schermataInizio()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #pulisce lo schermo ad ogni ciclo 
        finestra.fill(BLACK)
        
        disegnaSfondo()

        #genera frutta e bombe casualmente
        generaFrutta(all_sprites, frutta_group)
        generaBombe(all_sprites, bomba_group)

        #movimento della spada in base alla posizione del mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        spada.rect.x = mouse_x - spada.rect.width / 2
        spada.rect.y = mouse_y - spada.rect.height / 2 

        disegnaVite(bombe_colpite, MAX_COLPI_BOMBE) #mette 3 cuori in alto che sarebbero le 3 vite

        #verifica le collisioni con la frutta o con le bombe
        punti = collisioniFrutta(punti, spada, frutta_group)   
        bombe_colpite = collisioniBombe(spada, bomba_group, bombe_colpite) #restituisce True se ha colpito meno di 3 bombe se no False

        if bombe_colpite >= MAX_COLPI_BOMBE:
            if fineGioco(punti): #fineGioco funzione che restituisce True o False se vuoi riniziare una partita 
                punti = 0
                bombe_colpite = 0
                all_sprites.empty() #funzione che 
                frutta_group.empty()
                bomba_group.empty()
                spada = Spada(0, 0)
                all_sprites.add(spada)
                running = True
            else:
                running = False

        all_sprites.update() #aggiorna tutte le sprite facendole muovere

        all_sprites.draw(finestra) #disegna tutte le sprite sulla finestra

        scrivePunteggio(punti)

        pygame.display.flip() #aggiorna la finestra di gioco

        clock.tick(60) #imposta fps

    #chiude Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()