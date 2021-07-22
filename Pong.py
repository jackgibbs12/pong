import pygame
from random import randint

pygame.init()

#Define variables
screen_width = 600
screen_height = 800

fps = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")


class Paddle():
    def __init__(self, xIn, paddleIn):
        self.paddle = paddleIn
        self.x = xIn
        self.y = 0


    def move(self):
        """
        Method to check if the paddle is to be moved due to key input
        """
        
        key = pygame.key.get_pressed()

        if self.paddle == 1:
            #If down key is pressed, move the paddle down by 10 providing the paddle is not at the bottom
            if key[pygame.K_DOWN] and self.y < screen_height:
                self.y +=10

            #If up key is pressed, move the paddle up by 10 providing the paddle is not at the top
            if key[pygame.K_UP] and self.y >0:
                self.y -=10
        else:
            #If down key is pressed, move the paddle down by 10 providing the paddle is not at the bottom
            if key[pygame.K_s] and self.y < screen_height:
                self.y +=10

            #If up key is pressed, move the paddle up by 10 providing the paddle is not at the top
            if key[pygame.K_w] and self.y >0:
                self.y -=10
            


    def draw(self):
        """
        Method to draw the paddle to the screen
        """
        
        #Draw the paddle to the screen with the corresponding x and y positions
        rectangle = pygame.Rect(self.x, self.y, 20, 80)
        pygame.draw.rect(screen, (255,255,255), rectangle)

class Ball():
    def __init__(self):
        self.x = 30
        self.y = 30
        self.velocity = [randint(4,8), randint(4,8)]

    def update(self):
        """
        Method to update the position of the ball
        """
        
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        #Check if the ball has hit the edge and change its direction
        if self.x <=0:
            self.velocity[0] = -self.velocity[0]
        if self.x >=600:
            self.velocity[0] = -self.velocity[0]

        if self.y <=0:
            self.velocity[1] = -self.velocity[1]
        if self.y >=800:
            self.velocity[1] = -self.velocity[1]

    def draw(self):
        """
        Method to draw the ball to the screen
        """
        
        pygame.draw.circle(screen,(255,255,255),(self.x,self.y),10)
        
        
        
#Instantiate two paddle objects with corresponding x values, and a ball object
paddle1 = Paddle(30, 1)
paddle2 = Paddle(550, 2)

ball = Ball()


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

    #Move and draw the ball
    ball.update()
    ball.draw()
    
    pygame.display.update()
    clock.tick(fps)

    #Check if the user exits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()


