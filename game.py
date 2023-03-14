import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((622, 311))
pygame.display.set_caption('Zombie Attack By Tregz')
icon = pygame.image.load('images/zombie.png')
pygame.display.set_icon(icon)

background = pygame.image.load('background/imgonline-com-ua-Resize-mNh0THduZ2.jpg').convert()

# Player
walk_right = [
    pygame.image.load('player/player_right/1.png').convert_alpha(),
    pygame.image.load('player/player_right/2.png').convert_alpha(),
    pygame.image.load('player/player_right/3.png').convert_alpha(),
    pygame.image.load('player/player_right/4.png').convert_alpha(),
    pygame.image.load('player/player_right/5.png').convert_alpha()
]


# Enemies
zombie = pygame.image.load('enemies/treasure.png').convert_alpha()
#zombie_x = 624
zombie_list = []

player_anim_count = 0
background_x = 0

player_speed = 10
player_x = 150
player_y = 140

is_jump = False
jump_count = 9

sound = pygame.mixer.Sound('sounds/sound.mp3')
#sound.play()

zombie_timer = pygame.USEREVENT + 1
pygame.time.set_timer(zombie_timer, 3000)

running = True
while running:

    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 622, 0))
    #screen.blit(zombie, (zombie_x, 180))

    player_rect = walk_right[0].get_rect(topleft=(player_x, player_y))

    if zombie_list:
        for el in zombie_list:
            screen.blit(zombie, el)
            el.x -= 10

            if player_rect.colliderect(el):
                print('You lose')

    screen.blit(walk_right[player_anim_count], (player_x, player_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 5:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 500:
        player_x += player_speed

    if not is_jump:
        if keys[pygame.K_UP]:
            is_jump = True
    else:
        if jump_count >= -9:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 9

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    background_x -= 2
    if background_x == -622:
        background_x = 0

    #zombie_x -= 10

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == zombie_timer:
            zombie_list.append(zombie.get_rect(topleft=(622, 180)))

    clock.tick(15)
