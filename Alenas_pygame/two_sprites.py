import pygame
import sys

# Initialisera Pygame
pygame.init()

# Ange fönstrets dimensioner
width, height = 800, 600

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

# Skapa en spriteklass
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

        # Anropa konstruktorn för Spriteklassen
        super().__init__()

        # Skapa en yta för spelaren
        self.image = pygame.Surface((25, 50))

        # Fyll ytan med en färg
        self.image.fill(color)

        # Hämta rektangeln som omger ytan
        self.rect = self.image.get_rect()
        # Placera spelaren vid x, y på skärmen
        self.rect.center = (x, y)

        # Ladda dina bilder för olika riktningar
        self.image_up = pygame.image.load("images/uppåt.png").convert_alpha()
        self.image_down = pygame.image.load("images/nedåt.png").convert_alpha()

        # Ändra storleken på bilden att matcha spelarytan
        self.image_up = pygame.transform.scale(self.image_up, (25, 50))
        self.image_down = pygame.transform.scale(self.image_down, (25, 50))

        # Sätt den aktuella bilden till den som är för uppåtrörelse som standard
        self.image = self.image_up

    def draw(self, surface):
        # Ändra färgen för ritning
        #self.color = (0, 255, 0)  # Ny färg
        #self.image.fill(self.color)  # Uppdatera färgen på ytan
        surface.blit(self.image, self.rect)

    def move(self, keys):
        # logik för spelarens rörelse eller andra uppdateringar
        # Kontrollera tangenttryckningar för att styra spelaren
        speed = 5
        dy = 0
        up = None
        if self == player1:
            if keys[pygame.K_s]:
                dy -= speed
                up = True
            if keys[pygame.K_z]:
                dy += speed
                up = False

        if self == player2:
            if keys[pygame.K_UP]:
                dy -= speed
                up = True
            if keys[pygame.K_DOWN]:
                dy += speed
                up = False

        # kontrollera så att spelaren är på skärmen
        if up is not None:
            if self.rect.top + dy < 0:
                dy = -self.rect.top
            if self.rect.bottom + dy > height:
                dy = height - self.rect.bottom

        # uppdatera spelarens position och bild
            self.rect.y += dy
            if up:
                self.image = self.image_up
            else:
                self.image = self.image_down

# Skapa en instans av spelaren och lägg till en grupp
all_sprites = pygame.sprite.Group()
player1 = Player(200, height / 2, (255,0,0))
player2 = Player(500, height / 2, (255,255,255))
all_sprites.add(player1)
all_sprites.add(player2)

#Välj bild att använda som bakgrund
background_image = pygame.image.load("images/bakgrund.jpg").convert_alpha()

#funktion för att rita bakgrund
def draw_background():
    scaled_background = pygame.transform.scale(background_image, (width, height))
    screen.blit(scaled_background, (0,0))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Inside the game loop
    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move players
    player1.move(keys)
    player2.move(keys)

    # Rensa skärmen
    screen.fill((0, 0, 0))

    # Rita bakgrunden först
    draw_background()

    # Uppdatera alla sprites
    all_sprites.update()

    # Draw all sprites onto the screen
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    clock.tick(fps)

# Quit Pygame
pygame.quit()
sys.exit()
