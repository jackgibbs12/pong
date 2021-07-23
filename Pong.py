import pygame
from random import randint

pygame.init()

#Define variables
screen_width = 600
screen_height = 600

fps = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
font = pygame.font.SysFont('Comic Sans MS', 30)
white = (254,254,254)

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
            if key[pygame.K_DOWN] and self.rect.y < screen_height - 80:
                self.rect.y += 10

            #If up key is pressed, move the paddle up by 10 providing the paddle is not at the top
            if key[pygame.K_UP] and self.rect.y > 0:
                self.rect.y -= 10
        else:
            #If down key is pressed, move the paddle down by 10 providing the paddle is not at the bottom
            if key[pygame.K_s] and self.rect.y < screen_height - 80:
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
        self.rect.x = 300
        self.rect.y = 300

        #Set the velocity of the ball in the x and y direction randomly
        self.velocity = [randint(3,6), randint(3,6)]

    def updateBall(self, player1Score, player2Score):
        """
        Method to update the position of the ball
        """
        
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


        #Check if the ball has hit the edge and change its direction
        if self.rect.x <= 0:
            self.velocity[0] = - self.velocity[0]
            player2Score += 1
        if self.rect.x >= 600:
            self.velocity[0] = - self.velocity[0]
            player1Score += 1

        if self.rect.y <= 0:
            self.velocity[1] = - self.velocity[1]
        if self.rect.y >= 600:
            self.velocity[1] = - self.velocity[1]

        return player1Score, player2Score

    def bounce(self):
        """
        Method to handle when the ball comes into contact with a paddle
        """
        
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-3,6)

def playGame():
        
    #Instantiate two paddle objects with corresponding x values, and a ball object
    paddle1 = Paddle(30, 200, 1)
    paddle2 = Paddle(550,400, 2)
    ball = Ball()

    #Add the paddles and the ball to a list of all sprites
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(paddle1)
    all_sprites_list.add(paddle2)
    all_sprites_list.add(ball)

    #Initialise player scores
    player1Score = 0
    player2Score = 0 

    run = True
    while run:

        #Draw the sprites to the screen
        all_sprites_list.update()
        all_sprites_list.draw(screen)
       
        pygame.display.flip()

        #Move and draw the two paddles and the ball
        paddle1.move()
        paddle2.move()
        player1Score, player2Score = ball.updateBall(player1Score, player2Score)
        
        #Check if the ball has collided with a padle
        if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
            ball.bounce()

        #Fill the background and draw the middle line on the screen
        screen.fill((1,1,1))
        pygame.draw.line(screen, (255,255,255), [300, 0], [300, 800], 5)
        screen.blit(font.render(str(player1Score), True, ((255,255,255))), (250, 20))
        screen.blit(font.render(str(player2Score), True, ((255,255,255))), (350, 20))

        clock.tick(fps)

        #Check if the user exits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def mainMenu():
    """
    Function to display a main menu with three options:
    New Game
    Rules and Controls
    Quit
    """

    #Render options to the screen
    screen.fill((1,1,1))
    screen.blit(font.render('New Game', True, ((255,255,255))), (60, 100))
    screen.blit(font.render('Rules and Controls', True, ((255,255,255))), (60, 200))
    screen.blit(font.render('Quit', True, ((255,255,255))), (60, 300))

    #Check for user clicking options on the menu
    waiting = True
    while waiting:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                mainGameLoop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 60 <mouseX < 300 and 100 < mouseY < 150:
                     #Selected to play a new game
                     waiting = False
                     playGame()
                if 60 <mouseX < 400 and 200 < mouseY < 250:
                    #Selected to open the rules and controls
                    waiting = False
                    #Add rules and controls functionality here!
                if 60 <mouseX < 300 and 300 < mouseY < 350:
                    #Selected to quit
                    waiting = False
                    
        pygame.display.flip()
        clock.tick(fps)

mainMenu()           
pygame.quit()


