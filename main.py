
import pygame
import sys
import time
from math import atan2, cos, sin
from Player import Player
from tankbase import draw_tank_base
from Ally import Ally, allies
from Utilities import *
from jet1 import jet1group
from jet2 import jet2group
from BomberRight import bomber_right_group
from BomberLeft import bomber_left_group
from Explosion import explosions, Explosion

pygame.init()

# Create the screen:
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Convoy Defense')

# Create default settings:
clock = pygame.time.Clock()
game_timer = 0
score = 0
level = 1
bullet_threshold = 0
score_font = pygame.font.Font("./assets/Kachusha.ttf", 30)
welcome_font = pygame.font.Font("./assets/kremlin.ttf", 50)

# Creating the background:
background = SCREEN.copy()
draw_background(background)  # Draws all background tiles on a copy of the screen

# Menu Page
menu = True
while menu:
    menu = pygame.image.load("./assets/titlepage.jpg")
    menu = pygame.transform.scale(menu, (1025, 1025))
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(menu, ((SCREEN_WIDTH/2 - menu.get_width()/2), (SCREEN_HEIGHT/2 - menu.get_height()/2) + 170))
    menu_text_1 = welcome_font.render('PRESS "SPACE" TO BEGIN', True, (220, 0, 0))
    menu_text_2 = welcome_font.render('EXIT THE WINDOW TO QUIT', True, (220, 0, 0))
    SCREEN.blit(menu_text_1, (SCREEN_WIDTH / 2 - menu_text_1.get_width() / 2,
                              SCREEN_HEIGHT - 120))
    SCREEN.blit(menu_text_2, (SCREEN_WIDTH / 2 - menu_text_2.get_width() / 2,
                              SCREEN_HEIGHT - 50))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(power_up)
                menu = False


# Play music
pygame.mixer.music.set_volume(.75)
pygame.mixer.music.load("./sounds/subbase.mp3")
pygame.mixer.music.queue("./sounds/whiskeyhoteltrim.mp3")
pygame.mixer.music.play(0, 0, 0)

# Load Player:
player = Player()

# Add road strip and other assets:
add_strips(1)

humvee_1 = Ally(SCREEN_WIDTH/2, 60, './assets/humvee.png', .38)
humvee_2 = Ally(SCREEN_WIDTH/2, 175, './assets/humvee.png', .38)
mrap = Ally(SCREEN_WIDTH/2, SCREEN_HEIGHT - 95, './assets/mrap.png', .7)
allies.add(humvee_1, humvee_2, mrap)
allies_alive = [humvee_1, humvee_2, mrap]  # List of allies that are still alive in game, updates throughout

for i in range(0, 5):  # Add jets with a set x coordinate to fly towards (all allies have same x).
    #  Also each instance of this loop a jet is added with a random ally y-coordinate. The ally must be in the
    #  list to be chosen so if an ally is destroyed it can not be targeted
    add_jet1s_right(1, (SCREEN_WIDTH / 2),
                    (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])

for i in range(0, 4):  # Add jets with a set x coordinate to fly towards (all allies have same x).
    #  Also each instance of this loop a jet is added with a random ally y-coordinate. The ally must be in the
    #  list to be chosen so if an ally is destroyed it can not be targeted
    add_jet2s_left(1, (SCREEN_WIDTH / 2),
                   (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])

for i in range(0, 2):  # Add bombers with a set x coordinate to fly towards (all allies have same x).
    #  Also each instance of this loop a jet is added with a random ally y-coordinate. The ally must be in the
    #  list to be chosen so if an ally is destroyed it can not be targeted
    add_bomber_right(1, (SCREEN_WIDTH / 2),
                     (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])


for i in range(0, 2):  # Add bombers with a set x coordinate to fly towards (all allies have same x).
    #  Also each instance of this loop a jet is added with a random ally y-coordinate. The ally must be in the
    #  list to be chosen so if an ally is destroyed it can not be targeted
    add_bomber_left(1, (SCREEN_WIDTH / 2),
                    (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])

# Flag:
start_text = True

# Main Loop
while len(allies_alive) > 0:
    while start_text:
        SCREEN.blit(background, (0, 0))  # Draw the background
        draw_tank_base(SCREEN)  # Draw the base of the tank
        allies.draw(SCREEN)  # Draw the convoy
        SCREEN.blit(player.image, (SCREEN_WIDTH/2 - player.image.get_width()/2,
                                   SCREEN_HEIGHT/2 - player.image.get_height()/2))  # Draw a default position
        # Render text
        welcome_text = welcome_font.render('CONVOY DEFENSE', True, (220, 0, 0))
        SCREEN.blit(welcome_text, (SCREEN_WIDTH/2 - welcome_text.get_width()/2,
                                   SCREEN_HEIGHT/2 - welcome_text.get_height()/2))  # Draw text
        pygame.display.flip()  # Updates the display

        time.sleep(2)

        SCREEN.blit(background, (0, 0))  # Draw the background
        draw_tank_base(SCREEN)  # Draw the base of the tank
        allies.draw(SCREEN)  # Draw the convoy
        SCREEN.blit(player.image, (SCREEN_WIDTH / 2 - player.image.get_width() / 2,
                                   SCREEN_HEIGHT / 2 - player.image.get_height() / 2))  # Draw a default position
        # Render text
        instruction_text = score_font.render('\n Left click to fire.'
                                             ' Exit the window to quit.', True, (220, 0, 0))
        instruction_text_2 = score_font.render('Protect your trucks from the jets. Beat the clock to win.',
                                               True, (220, 0, 0))
        SCREEN.blit(instruction_text, (SCREEN_WIDTH / 2 - instruction_text.get_width() / 2,
                                       SCREEN_HEIGHT/2))  # Draw text
        SCREEN.blit(instruction_text_2, (SCREEN_WIDTH / 2 - instruction_text.get_width() / 2 - 115,
                                         SCREEN_HEIGHT - 200))  # Draw text
        pygame.display.flip()  # Updates the display
        time.sleep(8)
        start_text = False
    clock.tick(120)

    # Cycle through all possible events for QUIT or Fire Button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        current_time = pygame.time.get_ticks()
        if event.type == pygame.MOUSEBUTTONDOWN and current_time > bullet_threshold:
            # Every time mouse is clicked, new position taken, current time used for cooldown on shooting
            if pygame.mouse.get_pressed()[0]:
                pygame.mixer.Sound.play(shoot)
                bullet_threshold = 225 + current_time  # current_time must always be higher to shoot
                pos = player.turret_rect.center  # Turret center
                mouse_pos = pygame.mouse.get_pos()
                angle = (atan2(-(mouse_pos[1] - pos[1]), (mouse_pos[0] - pos[0])))  # Found angle between turret center
                # and mouse at the moment it was clicked
                turretRadius = 70  # figured out manually
                add_bullets(1, (pos[0] + turretRadius*cos(angle) - 10,
                                pos[1] - turretRadius*sin(angle) - 10))  # Using angle to offset bullet spawn

    SCREEN.blit(background, (0, 0))  # Draw new background after intro

    strips.update()  # Constantly update strip position
    strips.draw(SCREEN)  # Draw the strip
    bullets.update()
    draw_tank_base(SCREEN)  # Draw the base
    allies.draw(SCREEN)  # Draw allies
    bullets.draw(SCREEN)  # Draw bullets
    explosions.update()
    explosions.draw(SCREEN)
    player.update(SCREEN)  # This method tracks the mouse, calculates the angle,
    # rotates the turret accordingly, and redraws the turret on the screen

# Loop for Jet 1 Enemies
    for enemy in jet1group:
        enemy.update(- JET1_SPEED, 5, SCREEN)  # Set speed
        if enemy.rect.center[0] < -enemy.rect.width:  # If jet goes past screen width, remove it, make a new one
            jet1group.remove(enemy)
            add_jet1s_right(1, (SCREEN_WIDTH / 2),  # Same code as before: random ally selected to target
                            (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])
        if (enemy.rect.center[1] > SCREEN_HEIGHT + enemy.image.get_height()
                or enemy.rect.center[1] < 0 - enemy.image.get_height()):  # If jet goes above or below screen, remove
            jet1group.remove(enemy)
            add_jet1s_right(1, (SCREEN_WIDTH / 2),
                            (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])

# Loop for Jet 2 Enemies
    for enemy in jet2group:
        enemy.update(JET2_SPEED, 10, SCREEN)  # Set speed
        if enemy.rect.center[0] > SCREEN_WIDTH + enemy.rect.width:  # Remove if jet past screen, make a new one
            jet2group.remove(enemy)
            add_jet2s_left(1, (SCREEN_WIDTH / 2),  # Same code as before: random ally selected to target
                           (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])
        elif (enemy.rect.center[1] > SCREEN_HEIGHT + enemy.image.get_height()
                or enemy.rect.center[1] < 0 - enemy.image.get_height()):  # If jet goes above or below screen, remove
            jet2group.remove(enemy)
            add_jet2s_left(1, (SCREEN_WIDTH / 2),
                           (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])

# Loop for Bomber Right Enemies
    for enemy in bomber_right_group:
        enemy.update(- BOMBER_SPEED, 2, SCREEN)  # Set speed
        if enemy.rect.center[0] < -enemy.rect.width:  # If jet goes past screen width, remove it, make a new one
            bomber_right_group.remove(enemy)
            add_bomber_right(1, (SCREEN_WIDTH / 2),  # Same code as before: random ally selected to target
                             (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])
        if (enemy.rect.center[1] > SCREEN_HEIGHT + enemy.image.get_height()
                or enemy.rect.center[1] < 0 - enemy.image.get_height()):  # If jet goes above or below screen, remove
            bomber_right_group.remove(enemy)
            add_bomber_right(1, (SCREEN_WIDTH / 2),
                             (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])

# Loop for Bomber Left Enemies
    for enemy in bomber_left_group:
        enemy.update(BOMBER_SPEED, 2, SCREEN)  # Set speed
        if enemy.rect.center[0] > SCREEN_WIDTH + enemy.rect.width:  # If bomber past screen, remove
            bomber_left_group.remove(enemy)
            add_bomber_left(1, (SCREEN_WIDTH / 2),  # Same code as before: random ally selected to target
                            (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])
        if (enemy.rect.center[1] > SCREEN_HEIGHT + enemy.image.get_height()
                or enemy.rect.center[1] < 0 - enemy.image.get_height()):  # If jet goes above or below screen, remove
            bomber_left_group.remove(enemy)
            add_bomber_left(1, (SCREEN_WIDTH / 2),
                            (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])

    for bullet in bullets:
        for enemy in jet1group:
            bullet_enemy = pygame.sprite.spritecollide(bullet, jet1group, True)
            if bullet_enemy:
                score += len(bullet_enemy)
                pygame.mixer.Sound.play(jet1_hit)
                jet1group.remove(enemy)
                explosion = Explosion(enemy.rect.center[0], enemy.rect.center[1])
                explosions.add(explosion)
                add_jet1s_right(1, (SCREEN_WIDTH / 2),
                                (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])
                bullets.remove(bullet)

        for enemy in jet2group:
            bullet_enemy = pygame.sprite.spritecollide(bullet, jet2group, True)
            if bullet_enemy:
                score += len(bullet_enemy)
                pygame.mixer.Sound.play(jet2_hit)
                jet2group.remove(enemy)
                explosion = Explosion(enemy.rect.center[0], enemy.rect.center[1])
                explosions.add(explosion)
                add_jet2s_left(1, (SCREEN_WIDTH / 2),
                               (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])
                bullets.remove(bullet)

        for enemy in bomber_right_group:
            health_drop = pygame.sprite.spritecollide(bullet, bomber_right_group, False)
            if health_drop:
                enemy.health = enemy.health - 1  # Health drains per hit
                bullets.remove(bullet)
            if enemy.health < 1:
                pygame.mixer.Sound.play(bomber_hit)
                enemy.kill()  # Bomber killed when its health is less than 1 (0)
                bomber_right_group.remove(enemy)
                score = score + 3
                explosion = Explosion(enemy.rect.center[0], enemy.rect.center[1])
                explosions.add(explosion)
                add_bomber_right(1, (SCREEN_WIDTH / 2),
                                 (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])
                bullets.remove(bullet)

        for enemy in bomber_left_group:
            health_drop = pygame.sprite.spritecollide(bullet, bomber_left_group, False)
            if health_drop:
                enemy.health = enemy.health - 1  # Health drains per hit
                bullets.remove(bullet)
            if enemy.health < 1:
                pygame.mixer.Sound.play(bomber_hit)
                enemy.kill()  # Bomber killed when its health is less than 1 (0)
                bomber_left_group.remove(enemy)
                score = score + 3
                explosion = Explosion(enemy.rect.center[0], enemy.rect.center[1])
                explosions.add(explosion)
                add_bomber_left(1, (SCREEN_WIDTH / 2),
                                (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])
                bullets.remove(bullet)
    if len(jet2group) < 5:  # Redundancy to make sure enemies stay a certain number
        add_jet2s_left(1, (SCREEN_WIDTH / 2),
                       (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])
    if len(jet1group) < 5:
        add_jet1s_right(1, (SCREEN_WIDTH / 2),
                        (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])
    if len(bomber_right_group) < 5:
        add_bomber_right(1, (SCREEN_WIDTH / 2),
                         (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])
    if len(bomber_left_group) < 5:
        add_bomber_left(1, (SCREEN_WIDTH / 2),
                        (allies_alive[random.randint(0, len(allies_alive) - 1)]).rect.center[1])

    for ally in allies_alive:
        ally_jet1 = pygame.sprite.spritecollide(ally, jet1group, False)
        ally_jet2 = pygame.sprite.spritecollide(ally, jet2group, False)
        ally_bomber_left = pygame.sprite.spritecollide(ally, bomber_left_group, False)
        ally_bomber_right = pygame.sprite.spritecollide(ally, bomber_right_group, False)
        if ally_jet1 or ally_jet2 or ally_bomber_left or ally_bomber_right is True:
            explosion = Explosion(ally.rect.center[0], ally.rect.center[1])
            explosions.add(explosion)
            allies_alive.remove(ally)
            ally.kill()
            pygame.mixer.Sound.play(ally_hit)

    for strip in strips:
        if strip.rect.y == 0:  # When the top of the strip crosses the top of the screen, add a new one
            add_strips(1)
        if strip.rect.y > SCREEN_HEIGHT:  # When the top of the initial strip crosses the bottom, remove it
            strips.remove(strip)

    game_timer = game_timer + 1/60

    score_text = score_font.render(f"Score: {score}", True, (240, 0, 0))
    SCREEN.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 0))

    timer_text = score_font.render(f'Time: {222 - float(game_timer):.2f}', True, (240, 0, 0))
    SCREEN.blit(timer_text, (10, 0))

    level_text = score_font.render(f"Level: {level}", True, (240, 0, 0))
    SCREEN.blit(level_text, (10, SCREEN_HEIGHT - level_text.get_height()))

    if 30 <= game_timer < 60:
        level = 2
        JET1_SPEED = 4
        JET2_SPEED = 7
        BOMBER_SPEED = 2

    if 60 <= game_timer < 90:
        level = 3
        JET1_SPEED = 6
        JET2_SPEED = 11
        BOMBER_SPEED = 3

    if 90 <= game_timer < 130:
        level = 4
        JET1_SPEED = 7
        JET2_SPEED = 12
        BOMBER_SPEED = 4

    if 130 <= game_timer < 155:
        level = 5
        JET1_SPEED = 8
        JET2_SPEED = 13
        BOMBER_SPEED = 5

    if 155 <= game_timer < 170:
        level = 6
        JET1_SPEED = 10
        JET2_SPEED = 15
        BOMBER_SPEED = 6

    if 170 <= game_timer < 190:
        level = 7
        JET1_SPEED = 11
        JET2_SPEED = 16
        BOMBER_SPEED = 7

    if 190 <= game_timer < 200:
        level = 8
        JET1_SPEED = 12
        JET2_SPEED = 17
        BOMBER_SPEED = 8

    if 200 <= game_timer < 222:
        level = 9
        JET1_SPEED = 13
        JET2_SPEED = 18
        BOMBER_SPEED = 9

    if game_timer >= 222:
        SCREEN.blit(background, (0, 0))
        endtext = score_font.render('The Convoy Survived. You Won.', True, (240, 0, 0))
        SCREEN.blit(endtext, (SCREEN_WIDTH / 2 - endtext.get_width() / 2,
                              SCREEN_HEIGHT / 2 - endtext.get_height() / 2))
        scoretext = score_font.render(f'Final score: {score}', True, (240, 0, 0))
        SCREEN.blit(scoretext, (SCREEN_WIDTH / 2 - endtext.get_width() / 2,
                                SCREEN_HEIGHT / 2 - endtext.get_height() / 2 + 100))
        pygame.display.flip()
        time.sleep(5)
        break

    if len(allies_alive) == 0:
        SCREEN.blit(background, (0, 0))
        endtext = score_font.render('Convoy Destroyed. Game Over.', True, (240, 0, 0))
        SCREEN.blit(endtext, (SCREEN_WIDTH / 2 - endtext.get_width() / 2,
                              SCREEN_HEIGHT / 2 - endtext.get_height() / 2))
        scoretext = score_font.render(f'Final score: {score}', True, (240, 0, 0))
        SCREEN.blit(scoretext, (SCREEN_WIDTH / 2 - endtext.get_width() / 2,
                                SCREEN_HEIGHT / 2 - endtext.get_height() / 2 + 100))
        pygame.display.flip()
        time.sleep(5)
        break

    pygame.display.flip()  # Update the display after all changes are made
    clock.tick(60)  # Frame rate


SCREEN.blit(background, (0, 0))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
