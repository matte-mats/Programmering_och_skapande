import pygame

# Initialisera Pygame
pygame.init()

widht = 800
height = 600

# Skapa fönstret
screen = pygame.display.set_mode((widht, height))

# Ange färgen gul (RGB)
yellow = (255, 255, 0)

# Fyll fönstret med gul färg
screen.fill(yellow)

# Uppdatera fönstret
pygame.display.flip()

# Loop för att hålla fönstret öppet tills användaren stänger det
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # User clicked close button
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  # User pressed escape key

    screen.fill(yellow)
    pygame.display.flip()

pygame.quit()
