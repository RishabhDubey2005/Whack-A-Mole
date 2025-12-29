import pygame

# Buttons Class
class Buttons:
    
    # This constructor defines the attributes for each button instance
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) # Automatically scales size of button based on given inputs
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        
    # This Function will Draw the Button on the Screen:
    # Surface is the display screen for the game:
    def draw(self, surface):
        action = False # Indicates whether mouse action has occurred
        
        # Get the mouse's position
        pos = pygame.mouse.get_pos()
        
        # Check for if the mouse has been clicked:
        if (self.rect.collidepoint(pos)): # Account for button collisions
            if (pygame.mouse.get_pressed()[0] == 1) and (self.clicked == False):
                self.clicked = True
                action = True
        
        # Account for Resetting the Button (Button has NOT been clicked yet):
        if (pygame.mouse.get_pressed()[0] == 0):
            self.clicked = False
        
        # draw the button on the screen:
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return action