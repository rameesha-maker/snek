import pygame
import random
pygame.init()
window= pygame.display.set_mode((800,600))
pygame.display.set_caption("Its mine.andRameesha")

player= pygame.surface.Surface((100,100))
player.fill((250,250,250))
player_x = 0
player_y = 0
player_vel_x =0
player_vel_y = 0

falling_object = pygame.surface.Surface((50,50))
falling_object.fill((255,255,255))

falling_object_x = 5
falling_object_y = 0
falling_object_vel_x = 0
falling_object_vel_y = 0.3
game_state = 1


def collision_detection():
   return ((player_x <= falling_object_x + falling_object.width )and
   (player_x + player.width)>= falling_object_x and
   player_y <=(falling_object_y + falling_object.height +5 ) and 
   (player_y + player.height)>= falling_object_y)



while True:
   window.fill((23,53,64))
   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
            player_vel_x == -0.2
         if event.key == pygame.K_RIGHT:
            player_vel_x == 0.2
         
      else:
         player_vel_x = 0
         player_vel_y = 0


      if event.type == pygame.QUIT:
         quit(0)


   if collision_detection() :
      falling_object_y = 0
      falling_object_x = random.randint(0,window.width -50)


   if falling_object_y >=600:
      player_x , player_y = (1000,1000)
      player_vel_x , player_vel_y = 0,0

      falling_object_x ,falling_object_y = 1000,1000
      falling_object_vel_y ,falling_object_x = 0,0
      game_state = 2
   


   if game_state ==1:

   
      player_x += player_vel_x
      player_y += player_vel_y
      window.blit( player (player_x,player_y))

      falling_object_x += falling_object_vel_x
      falling_object_y += falling_object_vel_y
      window.blit( falling_object (falling_object_x,falling_object_y))
   elif game_state== 2:
      window.blit( game_over, (50,200))
   

   pygame.display.flip()












