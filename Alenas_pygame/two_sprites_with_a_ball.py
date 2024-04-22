import pygame
import sys
from ball import Ball
import random

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
pygame.display.set_caption("Minsk Sea 2")

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
        self.image_left = pygame.image.load("images/left.png").convert_alpha()
        self.image_right = pygame.image.load("images/right.png").convert_alpha()

        # Ändra storleken på bilden att matcha spelarytan
        self.image_left = pygame.transform.scale(self.image_left, (75, 50))
        self.image_right = pygame.transform.scale(self.image_right, (75, 50))

        # Sätt den aktuella bilden till den som är för uppåtrörelse som standard
        self.image = self.image_left

    def draw(self, surface):
        # Ändra färgen för ritning
        #self.color = (0, 255, 0)  # Ny färg
        #self.image.fill(self.color)  # Uppdatera färgen på ytan
        surface.blit(self.image, self.rect)

    def move(self, keys):
        # logik för spelarens rörelse eller andra uppdateringar
        # Kontrollera tangenttryckningar för att styra spelaren
        speed = 5
        dx = 0
        left = None
        if self == player1:
            if keys[pygame.K_s]: # Move left
                dx -= speed
                left = True
            if keys[pygame.K_a]: # Move right
                dx += speed
                left = False

        if self == player2:
            if keys[pygame.K_LEFT]:
                dx -= speed
                left = True
            if keys[pygame.K_RIGHT]:
                dx += speed
                left = False

        # kontrollera så att spelaren är på skärmen
        if left is not None:
            if self.rect.left + dx < 0:
                dx = -self.rect.left
            if self.rect.right + dx > width:
                dx = width - self.rect.right

        # uppdatera spelarens position och bild
            self.rect.x += dx
            if left:
                self.image = self.image_left
            else:
                self.image = self.image_right

# Skapa en instans av spelaren och lägg till en grupp
all_sprites = pygame.sprite.Group()
player1 = Player(200, height / 4, (255,0,0))
player2 = Player(500, height / 2.5, (255,255,255))
all_sprites.add(player1)
all_sprites.add(player2)

# Poängräkning för spelarna
score_player1 = 0
score_player2 = 0

# Skapa en font för poängräkning
font = pygame.font.Font(None, 36)

# Skapa en boll
ball = Ball(width, height, all_sprites)
all_sprites.add(ball)

# Draw a ball
screen.blit(ball.image, ball.rect)

def create_random_ball(screen_width, screen_height, other_sprites):
    radius = random.randint(5, 20)  # Random radius between 5 and 20
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color
    speed = random.randint(1, 4)  # Random speed between 3 and 7
    x = random.randint(radius, screen_width - radius)  # Random x position
    y = random.randint(radius, screen_height - radius)  # Random y position
    return Ball(screen_width, screen_height, other_sprites, radius, color, speed)

# Create four more balls
random_balls = [create_random_ball(width, height, all_sprites) for _ in range(3)]
all_sprites.add(random_balls)

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

    # Rita poängen för varje spelare i toppen av fönstret
    score_text_player1 = font.render("Spelare 1: " + str(score_player1), True, (255, 255, 255))
    score_text_player2 = font.render("Spelare 2: " + str(score_player2), True, (255, 255, 255))
    screen.blit(score_text_player1, (10, 10))  # Placera texten för spelare 1 i övre vänstra hörnet
    screen.blit(score_text_player2,
                (width - score_text_player2.get_width() - 10, 10))  # Placera texten för spelare 2 i övre högra hörnet

    # Update the display
    pygame.display.flip()

    # Kolla kollisioner med bollens rektangel
    if ball.rect.left <= 0:
        # Bollen träffade vänster kant, spelare 2 får poäng
        score_player2 += 1
        print("Spelare 2 poäng: ", score_player2)
        # Återställ bollens position
        ball.rect.center = (width // 2, height // 2)
        # Återställ bollens riktning
        ball.direction = [random.choice([-1, 1]), random.choice([-1, 1])]
    elif ball.rect.right >= width:
        # Bollen träffade höger kant, spelare 1 får poäng
        score_player1 += 1
        print("Spelare 1 poäng: ", score_player1)
        # Återställ bollens position
        ball.rect.center = (width // 2, height // 2)
        # Återställ bollens riktning
        ball.direction = [random.choice([-1, 1]), random.choice([-1, 1])]

    clock.tick(fps)

# Quit Pygame
pygame.quit()
sys.exit()
