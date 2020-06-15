import pygame
import random
pygame.init()

# colours
white = (255,255,255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 600

#Creating Window
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Snakes')
pygame.display.update()

#Game Specific Variables


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
hiscore = 0



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])



#Game Loop
def game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)
    score = 0
    init_velocity = 5
    snake_size = 10
    fps = 100
    snk_list = []
    snk_length = 1 
    with open('highScore.txt', 'r') as f:
        hiscore = f.read()
    
    while not exit_game:
        if game_over:
            with open('highScore.txt', 'w') as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen('Game Over! Press Enter to Continue', red, 120 ,250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
            
            
        
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
        
            snake_x += velocity_x
            snake_y += velocity_y 

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                snk_length += 5
                score += 10
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(20, screen_height - 20)
                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            text_screen('Score: ' + str(score),red,5,5)
            text_screen('High Score: ' + str(hiscore),red,500,5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x > screen_width or snake_y > screen_height or snake_x < 0 or snake_y < 0:
                game_over = True
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

game_loop()
pygame.quit()

quit()