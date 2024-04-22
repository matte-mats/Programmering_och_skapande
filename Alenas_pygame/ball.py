import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, other_sprites, radius=10, color=(255, 255, 255), speed=5):
        super().__init__()

        # Skärmens dimensioner
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Andra sprites
        self.other_sprites = other_sprites

        # Bollens egenskaper
        self.radius = radius
        self.color = color
        self.speed = speed

        # Skapa bollens yta
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA) # Use per-pixel alpha
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

        # Hämta rektangeln som omger ytan och placera bollen i mitten av skärmen
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))

        # Riktning för bollens rörelse (x, y)
        self.direction = [1, 1]

    def update(self):
        # Uppdatera bollens position baserat på dess riktning och hastighet
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

        # Kolla kollisioner med andra sprites
        collisions = pygame.sprite.spritecollide(self, self.other_sprites, False)
        for sprite in collisions:
            # Undvik att kolla om bollen kolliderar med sig själv
            if sprite != self:
                # Ändra riktningen baserat på kollisionens riktning
                if self.rect.centerx < sprite.rect.centerx:
                    self.direction[0] = -1  # Bollen kolliderade med en sprite till vänster
                else:
                    self.direction[0] = 1  # Bollen kolliderade med en sprite till höger
                if self.rect.centery < sprite.rect.centery:
                    self.direction[1] = -1  # Bollen kolliderade med en sprite ovanför
                else:
                    self.direction[1] = 1  # Bollen kolliderade med en sprite nedanför

        # Kolla om bollen träffar sidorna av fönstret och ändra riktning om så är fallet
        if self.rect.left <= 0:
            self.direction[0] = 1  # Ändra horisontell riktning för att undvika fastnat i vänsterkanten
        elif self.rect.right >= self.screen_width:
            self.direction[0] = -1  # Ändra horisontell riktning för att undvika fastnat i högerkanten

        if self.rect.top <= 0:
            self.direction[1] = 1  # Ändra vertikal riktning för att undvika fastnat i övre kanten
        elif self.rect.bottom >= self.screen_height:
            self.direction[1] = -1  # Ändra vertikal riktning för att undvika fastnat i nedre kanten