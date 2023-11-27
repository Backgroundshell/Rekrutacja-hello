import pygame
import random
ok = True

pygame.init()


def draw(player, plant, light, current_player_animation):
    win.blit(bg, (0, 0))
    #pygame.draw.rect(win, (255, 255, 255), player)
    #pygame.draw.rect(win, (0, 250, 0), plant)
    pygame.draw.rect(win, (random_r, random_g, random_b), light)


# light random RGB colour
random_r = random.randint(0, 255)
random_g = random.randint(0, 255)
random_b = random.randint(0, 255)

# Set up window dimensions
width, height = 1000, 800
win = pygame.display.set_mode((width, height))

# Set window name
pygame.display.set_caption("Game")

# Set background image and scale it
bg = pygame.image.load("C:\\PYHTON\\background.jpg")
bg = pygame.transform.scale(bg, (width, height))

# Set light image
light_im = pygame.image.load("C:\\PYHTON\\Sprite-0002.png")

# Set e button
button = pygame.image.load("C:\\PYHTON\\e-alphabet-icon.png")
button = pygame.transform.scale(button, (25, 25))

# Set plant width and height
plant_width = 70
plant_height = 70

# Set player width and height
player_width = 40
player_height = 60

# Set light with and height
light_width = 20
light_height = 30

# Set animation width and height
animation_w = 200
animation_h = 200

# Initial player position
x_player = (width - player_width) // 2
y_player = height - player_height

# Player velocity
player_vel = 7

# Keep track of animation frame
frame = 0
animation_speed = 7  # Smaller number = faster

# Keep track of animation frame
frame_plant = 0

# Getting random nums for spawning the plant
my_list_x_p = list(range((0 + plant_width) // 2, (width - plant_width) // 2))
random_x_element_p = random.choice(my_list_x_p)

my_list_y_p = list(range((0 + plant_height) // 2, (height - plant_height) // 2))
random_y_element_p = random.choice(my_list_y_p)

# Getting random nums for spawning the light
my_list_x_l = list(range((0 + light_width) // 2, (width - light_width) // 2))
random_x_element_l = random.choice(my_list_x_l)

my_list_y_l = list(range((0 + plant_height) // 2, (height - plant_height) // 2))
random_y_element_l = random.choice(my_list_y_l)

# Player, plant and light spawn points
player = pygame.Rect(200, height - player_height, player_width, player_height)

plant = pygame.Rect(random_x_element_p, random_y_element_p, plant_width, plant_height)

light = pygame.Rect(random_x_element_l, random_y_element_l, light_width, light_height)

# Set character idle animations
idle_left = [pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle left1.png"), (animation_w, animation_h)),
             pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle left2.png"), (animation_w, animation_h)),
             pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle left3.png"), (animation_w, animation_h)),
             pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle left4.png"), (animation_w, animation_h))]

idle_right = [pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle right1.png"), (animation_w, animation_h)),
              pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle right2.png"), (animation_w, animation_h)),
              pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle right3.png"), (animation_w, animation_h)),
              pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle right4.png"), (animation_w, animation_h))]

idle_up = [pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle up1.png"), (animation_w, animation_h)),
           pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle up2.png"), (animation_w, animation_h)),
           pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle up3.png"), (animation_w, animation_h)),
           pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle up4.png"), (animation_w, animation_h))]

idle_down = [pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle down1.png"), (animation_w, animation_h)),
             pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle down2.png"), (animation_w, animation_h)),
             pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle down3.png"), (animation_w, animation_h)),
             pygame.transform.scale(pygame.image.load("C:\\PYHTON\\idle\\idle down4.png"), (animation_w, animation_h))]

current_player_animation = idle_left  # Start with left animation

# Set plant animation width and height
animation_plant_w = 48 * 1.25

animation_plant_h = 72 * 1.25

none = pygame.transform.scale(pygame.image.load("C:\\PYHTON\\pumpkin animation\\Pumpkin5.png"), (animation_plant_w, animation_plant_h))

grow = [pygame.transform.scale(pygame.image.load("C:\\PYHTON\\pumpkin animation\\Pumpkin1.png"), (animation_plant_w, animation_plant_h)),
        pygame.transform.scale(pygame.image.load("C:\\PYHTON\\pumpkin animation\\Pumpkin2.png"), (animation_plant_w, animation_plant_h)),
        pygame.transform.scale(pygame.image.load("C:\\PYHTON\\pumpkin animation\\Pumpkin3.png"), (animation_plant_w, animation_plant_h)),
        pygame.transform.scale(pygame.image.load("C:\\PYHTON\\pumpkin animation\\Pumpkin4.png"), (animation_plant_w, animation_plant_h)),
        pygame.transform.scale(pygame.image.load("C:\\PYHTON\\pumpkin animation\\Pumpkin5.png"), (animation_plant_w, animation_plant_h))]

current_plant_animation = none

# Main game loop
run = True
animation_plant_var = False

while run:
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        elif key[pygame.K_e]:
            if player.colliderect(plant):
                animation_plant_var = True

    # Update player position
    if key[pygame.K_a]:
        current_player_animation = idle_left
        player.x -= player_vel
    if key[pygame.K_d]:
        current_player_animation = idle_right
        player.x += player_vel
    if key[pygame.K_w]:
        current_player_animation = idle_up
        player.y -= player_vel
    if key[pygame.K_s]:
        current_player_animation = idle_down
        player.y += player_vel

    # Set left and right screen boundaries for player
    player.x = max(0, player.x)
    player.x = min(width - player_width, player.x)

    # Set top and bottom screen boundaries for player
    player.y = max(0, player.y)
    player.y = min(height - player_height, player.y)

    draw(player, plant, light, current_player_animation)

    if player.colliderect(plant):
        win.blit(button, (random_x_element_p + 70, random_y_element_p))
    if animation_plant_var:
        frame_plant += 1
        if frame_plant < (len(grow) * 8):
            current_plant_animation = grow[frame_plant // 8]
        else:
            frame_plant = 0
            animation_plant_var = False

    # Check for collision and change color
    if player.colliderect(light):
        if not collision_occurred:
            # Change the color of the stationary rectangle to a new random color
            random_r = random.randint(0, 255)
            random_g = random.randint(0, 255)
            random_b = random.randint(0, 255)
            collision_occurred = True  # Set the collision flag

    # Draw the light image
    win.blit(light_im, (light.x - 25, light.y - 15))

    # Draw the plant image
    win.blit(current_plant_animation, (plant.x, plant.y))

    # Draw the player's current animation frame
    win.blit(current_player_animation[frame // animation_speed], (player.x - 80, player.y - 70))

    # Control the frame rate
    pygame.time.delay(18)
    # Increment the frame counter for animation
    frame = (frame + 1) % (len(current_player_animation) * animation_speed)

    pygame.display.update()

    # Reset the collision flag when no longer colliding
    if not player.colliderect(light):
        collision_occurred = False

pygame.quit()
