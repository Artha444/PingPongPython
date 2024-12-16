import pygame, sys, random
def ball_move():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        reset()
    if ball.right >= screen_width:
        reset()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_move():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_move():
    if opponent.top < ball.y:
        opponent.top += opponent_speed 
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def reset():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

# general setup
pygame.init()
clock = pygame.time.Clock()
# MAIN WINDOW
screen_width = 1708
screen_height = 920
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Ping Pong Game')

font = pygame.font.SysFont("Consolas", int(screen_width/20))

# OBJECT
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70, 15, 200)
opponent = pygame.Rect(3, screen_height/2 - 70, 15, 200)

bg_color = pygame.Color('green4')
light_grey = (200,200,200)

ball_speed_x = 9 * random.choice((1,-1))
ball_speed_y = 9 * random.choice((1,-1))
player_speed = 0
opponent_speed = 10

while True:
    # INPUT
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 10
            if event.key == pygame.K_UP:
                player_speed -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 10
            if event.key == pygame.K_UP:
                player_speed +=10

    player_move()
    ball_move()
    opponent_move()

    # VISUAL
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))

    # updating the window
    pygame.display.flip()
    clock.tick(60)