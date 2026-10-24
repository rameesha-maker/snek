import pygame
import random
from settings import *
pygame.init()
window= pygame.display.set_mode((800,600))
pygame.display.set_caption("snep")
clock= pygame.time.Clock()


def valid_position(shape,shape_x,shape_y):
   for block_x,block_y in shape:
      x= shape_x +block_x
      y = shape_y + block_y

      if x <0 or x>= COLS:
         return False
      if y>= ROWS:
         return False
      if y >= 0 and board[y][x]!=0:
         return False
   return True

board =[[0 for col in range(COLS)]for row in range(ROWS)]

while True:
   window.fill((23,53,64))
   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
            if valid_position(shape,shape_x -1,shape_y):
               shape_x -= 1
            
         if event.key == pygame.K_RIGHT:
            if valid_position(shape,shape_x +1,shape_y):
               shape+= 1
         
      else:
         player_vel_x = 0
         player_vel_y = 0


      if event.type == pygame.QUIT:
         quit(0)


   '''if collision_detection() :
      falling_object_y = 0
      falling_object_x = random.randint(0,window.width -50)


   if falling_object_y >=600:
      player_x , player_y = (1000,1000)
      player_vel_x , player_vel_y = 0,0

      falling_object_x ,falling_object_y = 1000,1000
      falling_object_vel_y ,falling_object_x = 0,0
      game_state = 2
   


   if game_state ==1:'''

   
   '''player_x += player_vel_x
      player_y += player_vel_y
      window.blit( player (player_x,player_y))

      falling_object_x += falling_object_vel_x
      falling_object_y += falling_object_vel_y
      window.blit( falling_object (falling_object_x,falling_object_y))
   elif game_state== 2:
      window.blit( game_over, (50,200))'''

   fall_timer += clock.get_time()
   if fall_timer>= fall_delay:
      shape_y += 1
      fall_timer= 0

   clock.tick(60)

   pygame.display.flip()












