import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((622, 350))
pygame.display.set_caption('Zombie Attack By Tregz')
icon = pygame.image.load('images/zombie.png')
pygame.display.set_icon(icon)

background = pygame.image.load('background/background.png')

walk_right = [
    pygame.image.load('player/player_right/1.png'),
    pygame.image.load('player/player_right/2.png'),
    pygame.image.load('player/player_right/3.png'),
    pygame.image.load('player/player_right/4.png'),
    pygame.image.load('player/player_right/5.png')
]

player_anim_count = 0
background_x = 0

player_speed = 10
player_x = 150

sound = pygame.mixer.Sound('sounds/sound.mp3')
sound.play()

running = True
while running:

    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 622, 0))
    screen.blit(walk_right[player_anim_count], (player_x, 240))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 5:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 500:
        player_x += player_speed

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    background_x -= 2
    if background_x == -622:
        background_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(10)
