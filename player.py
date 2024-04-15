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
        # Ladda dina bilder för olika riktningar
        self.image_up = pygame.image.load("images/uppåt.png").convert_alpha()
        self.image_down = pygame.image.load("images/nedåt.png").convert_alpha()

        # Sätt den aktuella bilden till den som är för uppåtrörelse som standard
        self.image = self.image_up




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
                up = True
            if keys[pygame.K_z]:
                dy += speed
                up = False
        if player == 2:
            if keys[pygame.K_UP]:
                dy -= speed
                up = True
            if keys[pygame.K_DOWN]:
                dy += speed
                up = False

        #kontrollera så att spelaren är på skärmen
        if self.rect.top + dy < 0:
            dy = -self.rect.top
        if self.rect.bottom + dy > height:
            dy = height - self.rect.bottom

        #uppdatera spelarens position och bild
        self.rect.y += dy
        if up:
            self.image = self.image_up
        else:
            self.image = self.image_down

