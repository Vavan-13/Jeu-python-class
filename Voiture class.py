import pygame 
import time   
import random

pygame.init() 
gray=(60,60,60)
black=(255,0,0) 
display=pygame.display.set_mode((1400,850))
pygame.display.set_caption("Peace and love racing")    

carimg=pygame.image.load("car.png")
position_carimg = carimg.get_rect()
position_carimg.center = 45, 95
backgroundleft=pygame.image.load("background.png")
backgroundright=pygame.image.load("background.png")
car_width=23

def background():
    display.blit(backgroundleft,(0, 0))
    display.blit(backgroundright,(1400, 0))

def loop():
    x=700 
    y=540 
    x_change=0 
    y_change=0
    policecar_speed=100 
    police=0   
    police_startx=random.randrange(300,(700-car_width))
    police_starty=-600
    police_width=23
    police_height=47

    bumped=False
    while not bumped: 
        for event in pygame.event.get():   
            if event.type==pygame.QUIT:   
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN: 
                if event.key==pygame.K_LEFT:
                    x_change=-10   
                if event.key==pygame.K_RIGHT: 
                    x_change=10     
            if event.type==pygame.KEYUP:   
                x_change=0
        x+=x_change

        display.fill(gray) 
        background()
        police_starty-=(policecar_speed/1.2)   
        policecar(police_startx,police_starty,police) 
        police_starty+=policecar_speed         
        car(x,y)   
        if x<300 or x>1100-car_width:       
            crash()

        if police_starty>800:     
            police_starty=0-police_height 
            police_startx=random.randrange(435,(1225-300)) 
            police=random.randrange(0,3)   

        if y<police_starty+police_height:
            if x > police_startx and x < police_startx + police_width or x + car_width > police_startx and x + car_width < police_startx + police_width :
                crash()

class policecar():
    def __init__(self,rect):
        self.rect = self.image.get_rect()

    def policecar(police_startx,police_starty,police):
        if police==0:
            police_come=pygame.image.load("car2.png") 
            position_police_com = carimg.get_rect()
        if police==1: 
            police_come=pygame.image.load("car3.png")
            position_police_com = carimg.get_rect()
        if police==2:
            police_come=pygame.image.load("car1.png") 
            position_police_com = carimg.get_rect()
        display.blit(police_come,(police_startx,police_starty))

 
class crash:
    def __init__(self,rect):
        self.rect = self.image.get_rect()  

def crash():       
    message_display("Tu as fait un accident !")

    def message_display(text):     
        large_text=pygame.font.Font("freesansbold.ttf",80) 
        textsurf,textrect=text_object(text,large_text) 
        textrect.center=((700),(300)) 
        display.blit(textsurf,textrect)
        pygame.display.update()
        time.sleep(3)     
        loop()     

    def text_object(text,font):    
        text_surface=font.render(text,True,black) 
        return text_surface,text_surface.get_rect()  

class car():
    def __init__(self, x, y):
        self.rect = self.image.get_rect()
    def car(x,y): 
        display.blit(carimg,(x,y))


def loop():
    x=700 
    y=540 
    x_change=0 
    y_change=0
    policecar_speed=100 
    police=0   
    police_startx=random.randrange(130,(700-car_width))
    police_starty=-600
    police_width=23
    police_height=47

    bumped=False
    while not bumped: 
        for event in pygame.event.get():   
            if event.type==pygame.QUIT:   
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN: 
                if event.key==pygame.K_LEFT:
                    x_change=-10   
                if event.key==pygame.K_RIGHT: 
                    x_change=10     
            if event.type==pygame.KEYUP:   
                x_change=0
        x+=x_change

        display.fill(gray) 
        background()
        police_starty-=(policecar_speed/1.2)   
        policecar(police_startx,police_starty,police) 
        police_starty+=policecar_speed         
        car(x,y)   
        if x<300 or x>1050-car_width:       
            crash()

        if police_starty>800:     
            police_starty=0-police_height 
            police_startx=random.randrange(435,(1225-300)) 
            police=random.randrange(0,3)   

        if y<police_starty+police_height:
            if x > police_startx and x < police_startx + police_width or x + car_width > police_startx and x + car_width < police_startx + police_width :
                crash()

        pygame.display.update() 
loop()
pygame.quit() 
quit()
