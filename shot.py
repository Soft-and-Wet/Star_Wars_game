from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from defs import calculationOfSpeed

SPEEDBULLET = 5

class Shot(Sprite):
    def __init__(self, coord1, coord2):
        Sprite.__init__(self)
        self.speed_x = 0
        self.speed_y = 0
        self.speed_x, self.speed_y = calculationOfSpeed(coord1, coord2, SPEEDBULLET)
        self.image = Surface((10, 5))
        self.image.fill((200, 10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = coord1[0]
        self.rect.y = coord1[1]

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, enemies, bloks):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.collide(enemies, bloks)

    def collide(self, enemies, bloks):
        for enemy in enemies:
            if collide_rect(self, enemy):
                enemy.kill()
                self.kill()
        for blok in bloks:
            if collide_rect(self, blok):
                self.kill()
