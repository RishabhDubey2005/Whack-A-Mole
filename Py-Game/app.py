import pygame
import random
import time
import buttons
import mole

# Setup of the Display Window
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Whack-A-Mole")
clock = pygame.time.Clock()
running = True

# Game Screen Logic Variables:
main_menu = True
game_paused = False
menu_state = "main"

# Game Variables:
cell_size = 150
grid_spacing = 10
hole_color = (139,69,19)
score = 0
start_time = 0
game_time = 60
mole_spawn_time = 0.8
mole_change_time = 0
current_visible_mole = None

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

# Load Game Sprites:
good_mole_img = pygame.image.load("Sprites/Good_Mole.png").convert_alpha()
bad_mole_img = pygame.image.load("Sprites/Bad_Mole.png").convert_alpha()
hammer_img = pygame.image.load("Sprites/hammer_cursor.png").convert_alpha()

# Create Button Instances:
play_button = buttons.Buttons(600, 360, play_img, 1.5)
help_button = buttons.Buttons(350, 360, help_img, 1.5)
exit_button = buttons.Buttons(850, 360, exit_img, 1.5)
back_button = buttons.Buttons(600, 460, back_img, 1.5)

# Create Game Instances:
good_mole = mole.Mole(0, 0, good_mole_img, 0.25, 'good')
bad_mole = mole.Mole(0, 0, bad_mole_img, 0.25, 'bad')
hammer_img = pygame.transform.scale(hammer_img, (75, 75))

# Game Functions:

# This function will display different texts within the game:
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
    
# This function will draw the game grid:
def draw_grid():
    screen_width, screen_height = screen.get_size()
    
    # Calculate the total grid size of a 4x4 grid/matrix:
    num_cells = 4
    grid_width = num_cells * cell_size + (num_cells - 1) * grid_spacing
    grid_height = num_cells * cell_size + (num_cells - 1) * grid_spacing
    
    # Calculate the offset to center the grid on the screen:
    offset_x = (screen_width - grid_width) // 2
    offset_y = (screen_height - grid_height) // 2
    
    for row in range(4):
        for col in range(4):
            x = col * (cell_size + grid_spacing) + offset_x
            y = row * (cell_size + grid_spacing) + offset_y
            pygame.draw.rect(screen, hole_color, (x, y, cell_size, cell_size))

# This function will will get the grid position based on mouse coordinates
def get_grid_position(mouse_pos, offset_x, offset_y):
    x,y = mouse_pos
    col = (x - offset_x) // (cell_size + grid_spacing)
    row = (y - offset_y) // (cell_size + grid_spacing)
    
    # Ensure the click is within the grid bounds:
    if (0 <= row < 4) and (0 <= col < 4):
        return row, col
    else:
        return None

# This function will will get the pixel position of a given grid cell:
def get_cell_pixel_position(row, col, offset_x, offset_y):
    x = col * (cell_size + grid_spacing) + offset_x
    y = row * (cell_size + grid_spacing) + offset_y
    return x, y
    
    
# Code for running the game
while running:
    
    screen.fill("white")
    
    # Check if the game is at the main menu:
    if main_menu == True:
        if menu_state == "main": # Checking at the current state of the game screen
            draw_text("Whack-A-Mole", font, txt_color, 500, 250)
            
            if (play_button.draw(screen)):
                menu_state = "play"
    
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
        
        if menu_state == "play":
            # Initialize game state on first entry
            if start_time == 0:
                start_time = time.time()
                score = 0
                mole_change_time = time.time()
                current_visible_mole = None  # Track which mole is visible
            
            screen.fill((124, 252, 0))
            draw_grid()
            
            # Calculate screen center offsets for grid
            screen_width, screen_height = screen.get_size()
            grid_width = 4 * cell_size + 3 * grid_spacing
            grid_height = 4 * cell_size + 3 * grid_spacing
            offset_x = (screen_width - grid_width) // 2
            offset_y = (screen_height - grid_height) // 2
            
            # Get current time and calculate remaining time
            current_time = time.time()
            elapsed_time = current_time - start_time
            remaining_time = game_time - elapsed_time
            
            # Switch to results screen if time is up
            if remaining_time <= 0:
                menu_state = "results"
            
            # Spawn new mole at intervals
            if current_time - mole_change_time > mole_spawn_time:
                mole_row = random.randint(0, 3)
                mole_col = random.randint(0, 3)
                mole_type = random.choice(['good', 'bad'])  # Randomly select mole type
                mole_x, mole_y = get_cell_pixel_position(mole_row, mole_col, offset_x, offset_y)
                mole_x += (cell_size - good_mole.image.get_width()) // 2
                mole_y += (cell_size - good_mole.image.get_height()) // 2
                
                # Update the appropriate mole position
                if mole_type == 'good':
                    good_mole.rect.topleft = (mole_x, mole_y)
                    current_visible_mole = 'good'
                else:
                    bad_mole.rect.topleft = (mole_x, mole_y)
                    current_visible_mole = 'bad'
                
                mole_change_time = current_time
            
            # Draw the currently visible mole
            if current_visible_mole == 'good':
                good_mole.draw(screen)
            elif current_visible_mole == 'bad':
                bad_mole.draw(screen)
            
            # Handle mouse clicks
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if current_visible_mole == 'good' and good_mole.is_clicked(mouse_pos):
                        score += 1
                        current_visible_mole = None  # Hide mole immediately
                    elif current_visible_mole == 'bad' and bad_mole.is_clicked(mouse_pos):
                        score -= 1
                        current_visible_mole = None  # Hide mole immediately
                if event.type == pygame.QUIT:
                    running = False
            
            # Draw fist cursor
            mouse_pos = pygame.mouse.get_pos()
            fist_rect = hammer_img.get_rect(center=mouse_pos)
            screen.blit(hammer_img, fist_rect.topleft)
            
            # Display timer
            timer_text = font.render(f"Time: {max(0, int(remaining_time))}s", True, txt_color)
            screen.blit(timer_text, (20, 20))
            
            # Display score
            score_text = font.render(f"Score: {score}", True, txt_color)
            screen.blit(score_text, (20, 70))
                
    # Event Handler for Quitting the Game + Other Key Binds:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    # flip() the display to put your work on the screen
    pygame.display.flip()

    #clock.tick(60) # Run the game at 60 FPS
    clock.tick(30) # Run the game at 30 FPS (Temp)
    clock = pygame.time.Clock()

pygame.quit()