import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()

#Initializing the display window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SquasPY")

#Starting coordinates of the paddle
rect_x = 400
rect_y = 580

#initial speed of the paddle
rect_change_x = 0
rect_change_y = 0

#initial position of the ball
ball_x = 50
ball_y = 50

#speed of the ball
ball_change_x = 5
ball_change_y = 5

puntos = 0

#draws the paddle. Also restricts its movement between the edges
#of the window.
def drawrect(screen,x,y,puntos_acumulados):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699
    tamanyo = [x,y,100,20]
    if int(puntos_acumulados) > 3:
        tamanyo = [x,y,50,10]
    pygame.draw.rect(screen,RED,tamanyo)
     

def drawball(screen,x,y,puntos_acumulados):
    ball_change_y = 5
    if x<0:
        x=0
        ball_change_x = ball_change_x * -1
    elif x>785:
        x=785
        ball_change_x = ball_change_x * -1
    elif y<0:
        y=0
        ball_change_y = ball_change_y * -1
    elif x>rect_x and x<rect_x+100 and y==565:
        ball_change_y = ball_change_y * -1
    elif y>600:
        ball_change_y = ball_change_y * -1                        
    
    size_ball = [x,y,15,15]
    if int(puntos)>2:
        size_ball = [x,y,5,5]
    pygame.draw.rect(screen,WHITE,size_ball)
    
#game's main loop    
done = False
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_change_x = -6
            elif event.key == pygame.K_RIGHT:
                rect_change_x = 6
            #elif event.key == pygame.K_UP:
                #rect_change_y = -6
            #elif event.key == pygame.K_DOWN:
                #rect_change_y = 6'''            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rect_change_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rect_change_y = 0            
    screen.fill(BLACK)
    rect_x += rect_change_x
    rect_y += rect_change_y
    
    ball_x += ball_change_x
    ball_y += ball_change_y
    
    
    #this handles the movement of the ball.
    if ball_x<0:
        ball_x=0
        ball_change_x = ball_change_x * -1
    elif ball_x>785:
        ball_x=785
        ball_change_x = ball_change_x * -1
    elif ball_y<0:
        ball_y=0
        ball_change_y = ball_change_y * -1
    elif ball_x>rect_x and ball_x<rect_x+100 and ball_y==565:
        ball_change_y = ball_change_y * -1
        puntos = puntos + 1
    elif ball_y>600:
        ball_change_y = ball_change_y * -1
        puntos = 0                        
    pygame.draw.rect(screen,WHITE,[ball_x,ball_y,5,5])
    
    drawball(screen,ball_x,ball_y,puntos)
    drawrect(screen,rect_x,rect_y,puntos)
    
    #Leyenda
    font= pygame.font.SysFont('Arial', 17, False, False)
    color_leyenda = BLACK
    if int(puntos) <= 2:
        color_leyenda = WHITE
    if int(puntos) > 2:
        color_leyenda = BLUE
    if int(puntos) > 5:
        color_leyenda = GREEN       
    text = font.render("Puntos = " + str(puntos) + ". Cada punto es rebote realizado", True, color_leyenda)
    chulla = font.render("Suma por rebote . Si toca suelo resetea.", True, WHITE)
    instrucciones = font.render("Mueve Flechas <-- y --> para desplazarte.", True, RED)
    screen.blit(text,[500,80]) 
    screen.blit(chulla,[500,50])
    screen.blit(instrucciones,[500,65])    
       
    pygame.display.flip()         
    clock.tick(60)
    
pygame.quit()    