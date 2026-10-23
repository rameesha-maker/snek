import pygame


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
falling_object_vel_y = 0
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         quit(0)
   
   
   window.fill((23,53,64))
   window.blit( player (player_x,player_y))

   pygame.display.flip()












pygame.init()