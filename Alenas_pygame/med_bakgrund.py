import pygame
from player2 import Player

# Initialisera Pygame
pygame.init()

# Ange fönstrets dimensioner
width = 800
height = 600

#Sätt uppdateringshastighet
clock = pygame.time.Clock()
fps = 60

# Skapa fönstret
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mitt Spel")

# Skapa en instans av spelaren
player1 = Player(200, height/2)
player2 = Player(700, height/2)

# Lägg till spelaren i en spritegrupp
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)

#Välj bild att använda som bakgrund
background_image = pygame.image.load("images/bakgrund.jpg").convert_alpha()

#funktion för att rita bakgrund
def draw_background():
    scaled_background = pygame.transform.scale(background_image, (width, height))
    screen.blit(scaled_background, (0,0))

# Spelhuvudloop
running = True
while running:
    # Hantera händelser
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rensa skärmen
    screen.fill((0, 0, 0))

    # Rita bakgrunden först
    draw_background()

    #Flytta spelarna
    player1.move()
    player2.move()

    # Uppdatera alla sprites
    all_sprites.update()

    # Rita alla sprites på skärmen
    all_sprites.draw(screen)

    # Uppdatera skärmen
    pygame.display.flip()

    clock.tick(fps)

# Avsluta Pygame
pygame.quit()