import pygame
from sprite_example import Player

# Initialisera Pygame
pygame.init()

# Ange fönstrets dimensioner
width = 800
height = 600

# Skapa fönstret
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mitt Spel")

# Skapa en instans av spelaren
player1 = Player(width // 3, height // 3)

# Lägg till spelaren i en spritegrupp
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)

# Spelhuvudloop
running = True
while running:
    # Hantera händelser
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Röra spelaren
    player1.move()

    # Uppdatera alla sprites
    all_sprites.update()

    # Rensa skärmen
    screen.fill((0, 0, 0))

    # Rita alla sprites på skärmen
    all_sprites.draw(screen)

    # Uppdatera skärmen
    pygame.display.flip()

# Avsluta Pygame
pygame.quit()