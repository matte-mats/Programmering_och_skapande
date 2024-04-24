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

#Ladda musik och ljud
pygame.mixer.music.load("sounds/bakgrund.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

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

# Spelhuvudloop
running = True
while running:
    # Hantera händelser
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rensa skärmen
    screen.fill((0, 0, 0))


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