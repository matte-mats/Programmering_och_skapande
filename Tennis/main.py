import pygame
import random
from player import Player
from ball import Ball

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
pygame.display.set_caption("Mats Spel")

# Skapa en instans av spelaren
player1 = Player(50, height/2)
player2 = Player(750, height/2)

# Lägg till spelaren i en spritegrupp
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)

# Skapa en boll
ball = Ball(width, height, all_sprites)
all_sprites.add(ball)

# Poängräkning för spelarna
score_player1 = 0
score_player2 = 0

# Skapa en font för poängräkning
font = pygame.font.Font(None, 36)

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

    # Använd spelarens update-metod för att uppdatera animationen
    player1.update()
    player2.update()

    # Använd spelarens update-metod för att uppdatera animationen
    player1.animate()
    player2.animate()

    # Flytta spelarna
    player1.move(height, 1)
    player2.move(height, 2)


    # Uppdatera alla sprites
    all_sprites.update()

    # Rita alla sprites på skärmen
    all_sprites.draw(screen)

    # Rita poängen för varje spelare i toppen av fönstret
    score_text_player1 = font.render("Spelare 1: " + str(score_player1), True, (255, 255, 255))
    score_text_player2 = font.render("Spelare 2: " + str(score_player2), True, (255, 255, 255))
    screen.blit(score_text_player1, (10, 10))  # Placera texten för spelare 1 i övre vänstra hörnet
    screen.blit(score_text_player2,
                (width - score_text_player2.get_width() - 10, 10))  # Placera texten för spelare 2 i övre högra hörnet

    # Uppdatera skärmen
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

# Avsluta Pygame
pygame.quit()

