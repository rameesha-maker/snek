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

def draw_board():
   for row in range(ROWS):
      for col in range(COLS):
         x = BOARD_X + col * BLOCK_SIZE
         y = BOARD_Y + row * BLOCK_SIZE
         rect = (x,y,BLOCK_SIZE,BLOCK_SIZE)
         if board[row][col] == 0:
            color = (30,45,60)
         else:
            color= (255,180,0)
      pygame.draw.rect(window,color,rect)
      pygame.draw.rect(window,(70,56,90),rect,1)

def draw_shape():
   for block_x,block_y in shape:
      x= BOARD_X +(shape_x +block_x)* BLOCK_SIZE
      y= BOARD_Y +(shape_y +block_y)* BLOCK_SIZE
      pygame.draw.rect(window,(0,200,255),(x,y,BLOCK_SIZE,BLOCK_SIZE))

while running:
   window.fill((23,53,64))

   dt = clock.tick(60)


   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
            if valid_position(shape,shape_x -1,shape_y):
               shape_x -= 1
            
         if event.key == pygame.K_RIGHT:
            if valid_position(shape,shape_x +1,shape_y):
               shape+= 1
   


      if event.type == pygame.QUIT:
         running = False


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

   fall_timer += dt
   if fall_timer>= fall_delay:
      shape_y += 1
      fall_timer= 0

   draw_board()
   draw_shape()

   pygame.display.flip()

pygame.quit()












