import pygame
import random
from settings import *
pygame.init()
window= pygame.display.set_mode((500,650))
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

board =[[0 for col in range(COLS)]
        for row in range(ROWS)]

def draw_board():
   for row in range(ROWS):
      for col in range(COLS):
         x = BOARD_X + col * BLOCK_SIZE
         y = BOARD_Y + row * BLOCK_SIZE
         rect = (x,y,BLOCK_SIZE,BLOCK_SIZE)
         if board[row][col] == 0:
            color = (30,40,50)
         else:
            color= (255,180,0)
      pygame.draw.rect(window,color,rect)
      pygame.draw.rect(window,(70,80,90),rect,1)

def draw_shape():
   for block_x,block_y in shape:
      x= BOARD_X +(shape_x +block_x)* BLOCK_SIZE
      y= BOARD_Y +(shape_y +block_y)* BLOCK_SIZE
      pygame.draw.rect(window,(0,200,255),(x,y,BLOCK_SIZE,BLOCK_SIZE))
      pygame.draw.rect(window,(255,255,255),(x,y,BLOCK_SIZE,BLOCK_SIZE),1)
running = True

def lock_shape(shape,shape_x,shape_y):
   for block_x,block_y in shape:
      x = shape_x + block_x
      y= shape_y +block_y
      if y>= 0:
         board[y][x]=1

def spawn_shape():
   return [(0,0),(1,0),(0,1),(1,1)],3,1

while running:
   window.fill((15,20,30))

   dt = clock.tick(60)


   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
            if valid_position(shape,shape_x -1,shape_y):
               shape_x -= 1
            
         if event.key == pygame.K_RIGHT:
            if valid_position(shape,shape_x +1,shape_y):
               shape_x += 1
         if event.key == pygame.K_DOWN:
            if valid_position(shape,shape_x,shape_y+1):
               shape_y +=1


      if event.type == pygame.QUIT:
         running = False

   fall_timer += dt
   if fall_timer>= fall_delay:
      if valid_position(shape,shape_x,shape_y +1):
         shape_y += 1


      else:
         lock_shape(shape,shape_x,shape_y)
         shape,shape_x,shape_y = spawn_shape()
      fall_timer= 0

   draw_board()
   draw_shape()

   pygame.display.flip()

pygame.quit()












