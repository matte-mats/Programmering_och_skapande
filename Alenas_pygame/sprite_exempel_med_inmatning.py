import pygame
import sys

# Initialisera Pygame
pygame.init()

# Ange fönstrets dimensioner
width = 800
height = 600

# Skapa fönstret
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Example")

# Skapa en spriteklass
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Röd färg för spelaren
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)  # Placera spelaren i mitten av skärmen

    def update(self):
        # Här kan du lägga till logik för spelarens rörelse eller andra uppdateringar
        pass

# Skapa en instans av spelaren
player = Player()

# Lägg till spelaren i en spritegrupp
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Spelhuvudloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Kontrollera tangenttryckningar för att styra spelaren
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            player.rect.x += 5
        if keys[pygame.K_UP]:
            player.rect.y -= 5
        if keys[pygame.K_DOWN]:
            player.rect.y += 5

        if keys[pygame.K_q]:
            running = False
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
sys.exit()