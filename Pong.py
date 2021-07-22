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


class Paddle(pygame.sprite.Sprite):
    def __init__(self, xIn,yIn, paddleIn):
        super().__init__()

        #Attribute to store whether paddle is number 1 or 2
        self.paddle = paddleIn

        #Draw the paddle as a rectangle and set its initial x and y position
        self.image = pygame.Surface([20,80])
        self.image.fill(white)
        self.image.set_colorkey(white)
        
        pygame.draw.rect(self.image, (255,255,255), [0, 0, 20, 80])
        
        self.rect = self.image.get_rect()
        self.rect.x = xIn
        self.rect.y = yIn


    def move(self):
        """
        Method to check if the paddle is to be moved due to key input
        """
        
        key = pygame.key.get_pressed()

        if self.paddle == 1:
            #If down key is pressed, move the paddle down by 10 providing the paddle is not at the bottom
            if key[pygame.K_DOWN] and self.rect.y < screen_height:
                self.rect.y += 10

            #If up key is pressed, move the paddle up by 10 providing the paddle is not at the top
            if key[pygame.K_UP] and self.rect.y > 0:
                self.rect.y -= 10
        else:
            #If down key is pressed, move the paddle down by 10 providing the paddle is not at the bottom
            if key[pygame.K_s] and self.rect.y < screen_height:
                self.rect.y += 10

            #If up key is pressed, move the paddle up by 10 providing the paddle is not at the top
            if key[pygame.K_w] and self.rect.y > 0:
                self.rect.y -= 10            


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #Draw the ball as a rectangle and set its initial x and y position
        self.image = pygame.Surface([20,20])
        self.image.fill(white)
        self.image.set_colorkey(white)
        
        pygame.draw.rect(self.image, (253,253,253), [0, 0, 20, 20])
        
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        #Set the velocity of the ball in the x and y direction randomly
        self.velocity = [randint(2,4), randint(2,4)]

    def update(self):
        """
        Method to update the position of the ball
        """
        
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


        #Check if the ball has hit the edge and change its direction
        if self.rect.x <= 0:
            self.velocity[0] = - self.velocity[0]
        if self.rect.x >= 600:
            self.velocity[0] = - self.velocity[0]

        if self.rect.y <= 0:
            self.velocity[1] = - self.velocity[1]
        if self.rect.y >= 800:
            self.velocity[1] = - self.velocity[1]

    def bounce(self):
        """
        Method to handle when the ball comes into contact with a paddle
        """
        
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-2,2)

        
white = (254,254,254)      
        
#Instantiate two paddle objects with corresponding x values, and a ball object
paddle1 = Paddle(30, 200, 1)
paddle2 = Paddle(550,600, 2)
ball = Ball()

#Add the paddles and the ball to a list of all sprites
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle1)
all_sprites_list.add(paddle2)
all_sprites_list.add(ball)

run = True
while run:

    #Draw the sprites to the screen
    all_sprites_list.update()
    all_sprites_list.draw(screen)
   
    pygame.display.flip()

    #Move and draw the two paddles and the ball
    paddle1.move()
    paddle2.move()
    ball.update()
    
    #Check if the ball has collided with a padle
    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
        ball.bounce()

    #Fill the background and draw the middle line on the screen
    screen.fill((1,1,1))
    pygame.draw.line(screen, (255,255,255), [300, 0], [300, 800], 5)

    
    clock.tick(fps)

    #Check if the user exits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()


