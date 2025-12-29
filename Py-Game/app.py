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
main_menu = True
game_paused = False
menu_state = "main"

# Define Fonts:
font = pygame.font.SysFont("arialblack", 40)
sub_font = pygame.font.SysFont("arialblack", 20)

# Define Colors:
txt_color = ("black")

# Load Button Sprites:
play_img = pygame.image.load("Sprites/Play_Button.png").convert_alpha()
help_img = pygame.image.load("Sprites/Help_Button.png").convert_alpha()
exit_img = pygame.image.load("Sprites/Exit_Button.png").convert_alpha()
back_img = pygame.image.load("Sprites/Back_Button.png").convert_alpha()

# Create Button Instances:
play_button = buttons.Buttons(600, 360, play_img, 1.5)
help_button = buttons.Buttons(350, 360, help_img, 1.5)
exit_button = buttons.Buttons(850, 360, exit_img, 1.5)
back_button = buttons.Buttons(600, 460, back_img, 1.5)


# This function will display different texts within the game:
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

# Code for running the game
while running:
    
    screen.fill("white")
    
    # Check if the game is at the main menu:
    if main_menu == True:
        if menu_state == "main": # Checking at the current state of the game screen
            draw_text("Whack-A-Mole", font, txt_color, 500, 250)
            
            if (play_button.draw(screen)):
                print("Play Button Present")
                # TODO: Link the button to the Game Screen: menu_state = "play"
    
            if (help_button.draw(screen)):
                menu_state = "help" # Change screen to the Help Screen
    
            # Exit the Game Upon User Action:
            if (exit_button.draw(screen)):
                running = False
        
        if menu_state == "help": # Menu State for the Help Screen Menu 
            draw_text("Help Menu:", font, txt_color, 500, 50)
            draw_text("Objective:", font, txt_color, 250, 125)
            draw_text("You are given 1 minute to whack as many moles as possible", sub_font, txt_color, 250, 200)
            draw_text("You are awarded 1 point for every correct mole they hit.", sub_font, txt_color, 250, 225)
            draw_text("You lose 1 point for every incorrect mole they hit.", sub_font, txt_color, 250, 250)
            draw_text("Once the timer is done, the game will show you your final score.", sub_font, txt_color, 250, 275)
            
            if (back_button.draw(screen)):
                menu_state = "main"
        '''
        if menu_state == "play":
        
        '''

        
    
    # Event Handler for Quitting the Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    # flip() the display to put your work on the screen
    pygame.display.flip()

    clock.tick(60) # Run the game at 60 FPS

pygame.quit()