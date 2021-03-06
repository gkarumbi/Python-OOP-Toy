import pygame 
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640,480]
BACKGROUND_COLOR = [255,255,255]


def debug_create_balls(object_list):
    ball = Ball(SCREEN_SIZE,Vector2(50,50),Vector2(3,3), [255,0,0],10)
    object_list.append(ball)


def debug_create_blocks(object_list):
    block =Block(SCREEN_SIZE,Vector2(100,100),20,20,[0,255,0])
    object_list.extend(block,)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    #manage how fast the screen updates

    clock = pygame.time.Clock()

    object_list =[]#list of objects

    debug_create_balls(object_list)
    debug_create_blocks(object_list)

    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
        
        for event in pygame.event.get():
            if event.type ==pygame.KEYDOWN:
                if event.key == pygmae.K_SPACE:
                    pass
        
        for ball in object_list:
            ball.update()

        #Draw loop
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen,pygame)

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()

    if __name__=="__main__":
        main()