'''
Program: Super Breakout!
Name: Taha Sarfraz
Date: 2022-12-07
Desc: This version of super breakout includes many new features.
Using classes for the bricks, the paddle, and the ball, the basic
features of the game are made. A second paddle is added for two-player
compatibility. Score and lives remaining are displayed at the top.

Background music is played, and sound effects are played whenever the ball
hits the paddle, the brick, and the bottom of the screen.
'''
import pygame
from classPaddle import Paddle
from classBall import Ball
from classBrick import Brick

pygame.init()

# Defining colors
LightBlue = (0,176,240)
Red = (255,0,0)
white = (255,255,255)
DarkBlue = (36,90,190)
Turquoise = (0,255,255)
Orange = (255,100,0)
Yellow = (255,255,0)
Purple = (138,43,226)
Black = (0,0,0)
DeepPink1 = (255,20,147)
Green = (0, 255, 0)
score = 0
lives = 3

# Open a new window
size = (1200, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pygame-breakout! by Taha")
# List that contains all sprites used in the game
sprites_game_list = pygame.sprite.Group()
# Create the ball sprite
ball = Ball(white,10,10)
ball.rect.x = 345
ball.rect.y = 400

# Draw 108 bricks. 18 in a row, 6 columns
bricks_list = pygame.sprite.Group()
for i in range(18):
    brick = Brick(DeepPink1,70,30)
    brick.rect.x = 30 + i* 60
    brick.rect.y = 60
    sprites_game_list.add(brick)
    bricks_list.add(brick)
for i in range(18):
    brick = Brick(Red,70,30)
    brick.rect.x = 30 + i* 60
    brick.rect.y = 100
    sprites_game_list.add(brick)
    bricks_list.add(brick)
for i in range(18):
    brick = Brick(Yellow,70,30)
    brick.rect.x = 30 + i* 60
    brick.rect.y = 140
    sprites_game_list.add(brick)
    bricks_list.add(brick)
for i in range(18):
    brick = Brick(Orange,70,30) #deeppink1 color (255,20,147)
    brick.rect.x = 30 + i* 60
    brick.rect.y = 180
    sprites_game_list.add(brick)
    bricks_list.add(brick)
for i in range(18):
    brick = Brick(Green,70,30)
    brick.rect.x = 30 + i* 60
    brick.rect.y = 220
    sprites_game_list.add(brick)
    bricks_list.add(brick)
for i in range(18):
    brick = Brick(Turquoise,70,30)
    brick.rect.x = 30 + i* 60
    brick.rect.y = 260
    sprites_game_list.add(brick)
    bricks_list.add(brick)
print(len(bricks_list))
# Create Paddle
paddle_width = 150
paddle = Paddle(LightBlue, paddle_width, 10)
paddle.rect.x = 350
paddle.rect.y = 710
# Create second paddle
paddle2 = Paddle(Orange, paddle_width, 10) #change color to black l8r
paddle2.rect.x = 550
paddle2.rect.y = 710

# Add paddle and ball to list containing all sprites
sprites_game_list.add(paddle)
sprites_game_list.add(ball)
sprites_game_list.add(paddle2)

# --- All Music and Sound Effects --- #
#background music
pygame.mixer.music.load('breakoutsong.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
#brick hit sound effect
brick_hit = pygame.mixer.Sound('brickhitsoundeffect.mp3')
brick_hit.set_volume(0.05)
#paddle hit sound effect
paddle_hit = pygame.mixer.Sound('paddlehitsound.mp3')
paddle_hit.set_volume(0.1)
#life lost sound effect
life_lost = pygame.mixer.Sound('lifelostsound.mp3')
life_lost.set_volume(0.9)
# I intentionally excluded sound effects for the win and loss screen of the game
# simply because I thought it'd be too many sound effects and would
# lower the quality of the game.

clock = pygame.time.Clock()
cont_Game = True
# -------- Main Program Loop ----------- #
while cont_Game:
    y = 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              cont_Game = False # Closes game if user quits

    # Moving le paddle using arrow user_keys
    user_keys = pygame.key.get_pressed()
    if user_keys[pygame.K_LEFT]:
        paddle.moveLeft(10)
    if user_keys[pygame.K_RIGHT]:
        paddle.moveRight(10)
    #Moving the second paddle when the user uses Z & X user_keys
    user_keys = pygame.key.get_pressed()
    if user_keys[pygame.K_z]:
        paddle2.moveLeft(10)
    if user_keys[pygame.K_x]:
        paddle2.moveRight(10)

    sprites_game_list.update()
    # Checks if ball bounces off the 4 walls, changes
    # velocity if it does.
    if ball.rect.x>=1200:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>800:
        life_lost.play()
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        # If game has ended, game over msg dispalyed for 3 seconds
        #and stops the game
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, white)
            pygame.mixer.music.set_volume(0.0)
            screen.blit(text, (450,300))
            pygame.display.flip()
            text = font.render("Lives: " + "0", 1, white)
            pygame.time.wait(5000)
            cont_Game=False
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]

    # Detect ball and paddle collision
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()
      paddle_hit.play()
    # Detect ball and paddle2 collision
    if pygame.sprite.collide_mask(ball, paddle2):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()
      paddle_hit.play()

    # Ball collision with brick detection
    brick_collision_list = pygame.sprite.spritecollide(ball,bricks_list,False)
    print(brick_collision_list)
    for brick in brick_collision_list:
      ball.bounce()
      brick_hit.play()
      score += 1
      brick.kill()
      # When half bricks remain, paddle width halves.
      if len(bricks_list)==0:
            # Display win msg for 3 secs
            font = pygame.font.Font(None, 74)
            text = font.render("~~You Win~~", 1, white)
            screen.blit(text, (450,300))
            pygame.display.flip()
            pygame.time.wait(5000)
            cont_Game=False


    # set screen to blue, and draw the long white line
    screen.fill(DarkBlue)
    pygame.draw.line(screen, white, [0, 38], [1200, 38], 2)

    # Display score and lives top part of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, white)
    screen.blit(text, (1100,10))

    sprites_game_list.draw(screen)
    pygame.display.flip()
    #limits to 60 fps
    clock.tick(60)

pygame.quit()
