import pygame
from pygame.locals import *
import random

size =width,height= (400,800)
road_w =int(width/1.6) 
roadmark_w = width/80
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4

pygame.init()

running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hero Khor")

screen.fill((60,220,0))
pygame.draw.rect(screen,(50,50,50),(width/2-road_w/2,0,road_w,height))
pygame.draw.rect(screen,(255,240,60),(width/2-roadmark_w/2,0,roadmark_w,height))
pygame.draw.rect(screen,(255,255,255),(width/2-road_w/2 + roadmark_w*2,0,roadmark_w,height))
pygame.draw.rect(screen,(255,255,255),(width/2+road_w/2 - roadmark_w*3,0,roadmark_w,height))



car = pygame.image.load('car.png')
car_loc=car.get_rect()
car_loc.center = right_lane,height*0.8

car2 = pygame.image.load('othercar.png')
car2_loc=car2.get_rect()
car2_loc.center = left_lane,height*0.2

#game loop
while running:
    car2_loc[1] += 1
    if car2_loc[1]> height:
        car2_loc[1]= -200
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane,-200
        else:
            car2_loc.center = left_lane ,-200
    if car_loc[0]==car2_loc[0]and car2_loc[1]>car_loc[1]-250:
        print("Game over u lo)se")
        running = False
    for event in pygame.event.get():
        if event.type==QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a,K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2,0)])
            if event.key in [K_d,K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2),0])

    pygame.draw.rect(screen,(50,50,50),(width/2-road_w/2,0,road_w,height))
    pygame.draw.rect(screen,(255,240,60),(width/2-roadmark_w/2,0,roadmark_w,height))
    pygame.draw.rect(screen,(255,255,255),(width/2-road_w/2 + roadmark_w*2,0,roadmark_w,height))
    pygame.draw.rect(screen,(255,255,255),(width/2+road_w/2 - roadmark_w*3,0,roadmark_w,height))


    screen.blit(car,car_loc)
    screen.blit(car2,car2_loc)
    pygame.display.update()

pygame.quit()