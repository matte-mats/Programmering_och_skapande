import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
    QUIT,
)
import sys
import random
from pygame.sprite import Group

# Initialisera Pygame
pygame.init()
pygame.font.init()

# Ange fönstrets dimensioner
width = 800
height = 600

#Sätt uppdateringshastighet
clock = pygame.time.Clock()
fps = 60

# Skapa fönstret
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Monkey in jungle")

#Välj bild att använda som bakgrund
background_image = pygame.image.load("Jungle.jpg").convert_alpha()

#funktion för att rita bakgrund
def draw_background():
    scaled_background = pygame.transform.scale(background_image, (width, height))
    screen.blit(scaled_background, (0,0))

#Ladda musik och ljud
pygame.mixer.music.load("Jungle_sound.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
coconut_collision_sound = pygame.mixer.Sound("Coconut_collision_sound.mp3")
enemy_collision_sound = pygame.mixer.Sound("Enemy_collision_sound.mp3")

# Skapa en spelare
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Anropa konstruktorn för Spriteklassen
        super().__init__()

        # Skapa en yta för spelaren
        self.image = pygame.Surface((80, 80))
        # Fyll ytan med bild
        self.image = pygame.image.load("Monkey v2.jpg")
        self.image = pygame.transform.scale(self.image, (60, 60))

        # Hämta rektangeln som omger ytan
        self.rect = self.image.get_rect()
        # Placera spelaren i mitten av skärmen längst ner
        self.rect.center = (width // 2, 550)


    def update(self):
        # logik för spelarens rörelse eller andra uppdateringar
        pass

class Coconut(pygame.sprite.Sprite):
    def __init__(self, screen):
        # Anropa konstruktorn för Spriteklassen
        super().__init__()
        self.screen = screen
        # Skapa en yta för spelaren
        self.image = pygame.Surface((20, 25))
       # Fyll ytan med bild
        self.image = pygame.image.load("Coconut.jpg")
        self.image = pygame.transform.scale(self.image, (20, 25))

        # Hämta rektangeln som omger ytan
        self.rect = self.image.get_rect()
        # Placera blocket i mitten av skärmen
        self.rect.center = (width // 2, 0)
        # Hastighetsvektor
        #self.velocity = pygame.Vector2(0, 1) 
        
        self.rect.x = random.randint(0, screen.get_width())  # Slumpmässig x-koordinat
        self.rect.y = 0  # Starta från toppen av skärmen
        self.speed = 1  # Fallhastighet
      
    def update(self):
        # Uppdatera positionen baserat på hastighetsvektorn
        self.rect.y += self.speed
        if self.rect.y > self.screen.get_height():
            self.kill()  # Ta bort blocket om det lämnar skärmen

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        # Anropa konstruktorn för Spriteklassen
        super().__init__()
        self.screen = screen
        # Skapa en yta för spelaren
        self.image = pygame.Surface((30, 30))
       # Fyll ytan med bild
        self.image = pygame.image.load("Enemy.jpg")
        self.image = pygame.transform.scale(self.image, (40, 40))

        # Hämta rektangeln som omger ytan
        self.rect = self.image.get_rect()
        # Placera blocket i mitten av skärmen
        self.rect.center = (width // 2, 0)
        # Hastighetsvektor
        #self.velocity = pygame.Vector2(0, 1) 
        
        self.rect.y = random.randint(0, screen.get_height())  # Slumpmässig y-koordinat
        self.rect.x = 0  # Starta från sidan av skärmen
        self.speed = 1  # Fallhastighet
      
    def update(self):
        # Uppdatera positionen baserat på hastighetsvektorn
        self.rect.x += self.speed
        if self.rect.x > self.screen.get_width():
            self.speed = -1
            if self.rect.x < self.screen.get_width():
                self.kill()  # Ta bort blocket om det lämnar skärmen



score = 0
score_increment_coconut = 1
score_increment_enemy = 10
    

player = Player()
# Lägg till spelaren i en spritegrupp
all_players = pygame.sprite.Group()
all_players.add(player)

coconut = Coconut(screen)
# Lägg till kokosnöten i en spritegrupp
all_coconuts = pygame.sprite.Group()
all_coconuts.add(coconut)

enemy = Enemy(screen)
# Lägg till enemy i en spritegrupp
all_enemies = pygame.sprite.Group()
all_enemies.add(enemy)

# Spelhuvudloop
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
             # Tangentbordsstyrning
            if event.key == K_LEFT:
                player.rect.move_ip(-50, 0)  # Flytta åt vänster
                if player.rect.x < 10:
                    player.rect.x = 10
            elif event.key == K_RIGHT:
                player.rect.move_ip(50, 0)  # Flytta åt höger
                if player.rect.x > 720:
                    player.rect.x = 720
            elif event.key == K_UP:
                player.rect.move_ip(0, -50)  # Flytta uppåt
                if player.rect.y < 10:
                    player.rect.y = 10
            elif event.key == K_DOWN:
                player.rect.move_ip(0, 50)  # Flytta nedåt
                if player.rect.y > 520:
                    player.rect.y = 520
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
     # Skapa nya kokosnötter slumpmässigt
    if random.randrange(100) < 2:
        new_coconut = Coconut(screen)
        all_coconuts.add(new_coconut)
    
      # Skapa nya enemies slumpmässigt
    if random.randrange(500) < 2:
        new_enemy = Enemy(screen)
        all_enemies.add(new_enemy)
    
    # Uppdatera kokosnötternas, enemies och spelarens positioner
    all_coconuts.update()
    all_players.update()
    all_enemies.update()

    # Rensa skärmen
    screen.fill((0, 0, 0))
    
     # Rita bakgrunden först
    draw_background()

    # Rita spelare, enemies och kokosnötter på skärmen
    all_coconuts.draw(screen)
    all_players.draw(screen)
    all_enemies.draw(screen)
    
    # Kolla efter kollisioner spelare och kokosnötter
    coconut_hit_list = pygame.sprite.spritecollide(player, all_coconuts, True)
    for coconut in coconut_hit_list:
        score += score_increment_coconut  # Öka poängen för varje kollision
        coconut_collision_sound.play() # Ljud för varje kollision


    # Kolla efter kollisioner spelare och enemies
    enemy_hit_list = pygame.sprite.spritecollide(player, all_enemies, True)
    for enemy in enemy_hit_list:
        score -= score_increment_enemy  # minska poängen för varje kollision
        enemy_collision_sound.play() # Ljud för varje kollision
        
    # Set up the font object
    font = pygame.font.Font(None, 36)
    # Render the score text
    text = font.render(f"Score: {score}", True, (255, 255, 255))  # White color
    # Position the text (centered horizontally)
    textpos = text.get_rect(centerx=screen.get_width() // 2)
    # Blit the text onto the screen
    screen.blit(text, textpos)

    # Uppdatera skärmen
    pygame.display.flip()
    
    clock.tick(fps)

# Avsluta Pygame
pygame.quit()

            
            

