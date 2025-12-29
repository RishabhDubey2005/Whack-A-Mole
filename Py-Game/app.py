import os
import pygame
import random
import time
import buttons

# Setup of the Display Window
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Whack-A-Mole")
clock = pygame.time.Clock()
running = True

# Game Variables:
main_menu = False
game_paused = False
menu_state = "main"

# Define Fonts:
font = pygame.font.SysFont("arialblack", 40)

# Define Colors:
txt_color = ("black")

# Load Button Sprites:
play_img = pygame.image.load("Sprites/Play_Button.png").convert_alpha()
help_img = pygame.image.load("Sprites/Help_Button.png").convert_alpha()
exit_img = pygame.image.load("Sprites/Exit_Button.png").convert_alpha()

# TODO: Create a Back Button to the Main Screen
back_img = pygame.image.load("Sprites/Help_Button.png").convert_alpha() # TODO: Create new sprite for back button

# Create Button Instances:
play_button = buttons.Buttons(600, 360, play_img, 1.5)
help_button = buttons.Buttons(350, 360, help_img, 1.5)
exit_button = buttons.Buttons(850, 360, exit_img, 1.5)
back_button = buttons.Buttons(850, 360, back_img, 1.5)


# This function will display different texts within the game:
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

# Code for running the game
while running:
    
    screen.fill("white")
    
    # Check if the game is at the main menu:
    if main_menu == True:
        draw_text("Test Screen", font, txt_color, 160, 250)
    else:
        draw_text("Whack-A-Mole", font, txt_color, 500, 250)
        
        if menu_state == "main": # Checking at the current state of the game screen
            if (play_button.draw(screen)):
                print("Play Button Present")
                # TODO: Link the button to the Game Screen
    
            if (help_button.draw(screen)):
                print("Help Button Present")
                # TODO: Link the button to the Help Screen
    
            # Exit the Game Upon User Action:
            if (exit_button.draw(screen)):
                running = False
    
    # Event Handler for Quitting the Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    # flip() the display to put your work on the screen
    pygame.display.flip()

    clock.tick(60) # Run the game at 60 FPS

pygame.quit()