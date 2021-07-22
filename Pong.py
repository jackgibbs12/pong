import pygame

pygame.init()

#Define variables
screen_width = 600
screen_height = 800

fps = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")


class Paddle():
    def __init__(self, x):     
        self.x = x
        self.y = 0


    def move(self):
        """
        Method to check if the paddle is to be moved due to key input
        """
        key = pygame.key.get_pressed()

        #If down key is pressed, move the paddle down by 10 providing the paddle is not at the bottom
        if key[pygame.K_DOWN] and self.y < screen_height:
            self.y +=10

        #If up key is pressed, move the paddle up by 10 providing the paddle is not at the top
        if key[pygame.K_UP] and self.y >0:
            self.y -=10


    def draw(self):
        """
        Method to draw the paddle to the screen
        """
        #Draw the paddle to the screen with the corresponding x and y positions
        rectangle = pygame.Rect(self.x, self.y, 20, 80)
        pygame.draw.rect(screen, (255,255,255), rectangle)
        
        
#Instantiate two paddle objects with corresponding x values
paddle1 = Paddle(30)
paddle2 = Paddle(550)


run = True
while run:
    #Fill the background and draw the middle line on the screen
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,255,255), [300, 0], [300, 800], 5)

    #Move and draw the two paddles
    paddle1.move()
    paddle1.draw()
    paddle2.move()
    paddle2.draw()
    
    pygame.display.update()
    clock.tick(fps)

    #Check if the user exits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()


