import pygame

# Initialisera Pygame
pygame.init()

# Ange fönstrets dimensioner
width = 800
height = 600

# Skapa fönstret
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mitt Spel")


# Skapa en spriteklass
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Anropa konstruktorn för Spriteklassen
        super().__init__()

        # Skapa en yta för spelaren
        self.image = pygame.Surface((50, 50))
        # Fyll ytan med en färg (t.ex. röd)
        self.image.fill((255, 0, 0))

        # Hämta rektangeln som omger ytan
        self.rect = self.image.get_rect()
        # Placera spelaren vid x, y på skärmen
        self.rect.center = (x,y)


    def move(self):
        # logik för spelarens rörelse eller andra uppdateringar
        # Kontrollera tangenttryckningar för att styra spelaren
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5


# Skapa en instans av spelaren
player = Player(200, 300)

# Lägg till spelaren i en spritegrupp
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Spelhuvudloop
running = True
while running:
    # Hantera händelser
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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