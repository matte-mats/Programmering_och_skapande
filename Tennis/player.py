import pygame

# Skapa en spriteklass
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Anropa konstruktorn för Spriteklassen
        super().__init__()

        # Skapa en yta för spelaren
        self.image = pygame.Surface((25, 50))
        # Fyll ytan med en färg (t.ex. röd)
        #self.image.fill((255, 0, 0))
        # Hämta rektangeln som omger ytan
        self.rect = self.image.get_rect()

        # Placera spelaren
        self.rect.center = (x, y)

        # Läs in hela spritesheeten som en yta
        self.spritesheet = pygame.image.load("images/player_spreadsheet.png").convert_alpha()

        # Klipp ut varje bild från spritesheeten och spara dem i en lista
        self.sprite_images = []
        sprite_width = 25  # Bredden på varje bild i spritesheeten
        sprite_height = 50  # Höjden på varje bild i spritesheeten
        for i in range(4):  # Antalet bilder i spritesheeten (t.ex. om det finns 4 bilder)
            rect = pygame.Rect(i * sprite_width, 0, sprite_width, sprite_height)
            image = self.spritesheet.subsurface(rect)
            self.sprite_images.append(image)

        # Använd den första bilden som standard
        self.image = self.sprite_images[0]

        # Skapa en rektangel som omger spelaren
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Variabel för att hålla reda på vilken bild som ska visas
        self.current_frame = 0

        # Variabel för att hålla reda på riktningen (upp/ned)
        self.direction = "up"

        self.animation_speed = 10  # Fördröjning mellan bildbyten

        self.animation_counter = 0  # Räknare för att spåra fördröjning

    def update(self):
        # Uppdatera bild baserat på riktning och nuvarande frame
        if self.direction == "up":
            self.image = self.sprite_images[self.current_frame]
        else:
            # Om spelaren rör sig nedåt, använd samma bilder men vänd dem
            self.image = pygame.transform.flip(self.sprite_images[self.current_frame], False, True)

        # Uppdatera position
        #self.rect.y += self.speed

    def animate(self):
        # Byt bild om det är dags enligt fördröjningen
        self.animation_counter += 1
        if self.animation_counter >= 10:
            self.animation_counter = 0  # Återställ räknaren
            self.current_frame = (self.current_frame + 1) % len(self.sprite_images)




    def draw(self, surface):
        # Ändra färgen för ritning
        #self.color = (0, 255, 0)  # Ny färg
        #self.image.fill(self.color)  # Uppdatera färgen på ytan
        surface.blit(self.image, self.rect)

    def move(self, height, player):
        # logik för spelarens rörelse eller andra uppdateringar
        # Kontrollera tangenttryckningar för att styra spelaren
        speed = 5
        keys = pygame.key.get_pressed()
        dy = 0
        up = True
        if player == 1:
            if keys[pygame.K_s]:
                dy -= speed
                self.direction = "up"
            if keys[pygame.K_z]:
                dy += speed
                self.direction = "down"
        if player == 2:
            if keys[pygame.K_UP]:
                dy -= speed
                self.direction = "up"
            if keys[pygame.K_DOWN]:
                dy += speed
                self.direction = "down"

        #kontrollera så att spelaren är på skärmen
        if self.rect.top + dy < 0:
            dy = -self.rect.top
        if self.rect.bottom + dy > height:
            dy = height - self.rect.bottom

        #uppdatera spelarens position och bild
        self.rect.y += dy

