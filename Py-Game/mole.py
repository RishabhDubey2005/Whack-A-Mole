import pygame

# Mole Class:
class Mole(pygame.sprite.Sprite):
    def __init__(self, x, y, image, scale, mole_type):
        super().__init__()
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.mole_type = mole_type  # 'good' or 'bad' mole
    
    def pop_up(self):
        # Logic for popping up the mole
        pass
    
    def hide(self):
        # Logic for hiding the mole
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    