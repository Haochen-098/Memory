# AUTHOR: HAOCHEN GOU


from uagame import Window
import random
import pygame, time
from pygame.locals import *


def main():
   
   window = Window('Memory', 500, 400)
   window.set_auto_update(False)
   game = Game(window)
   game.play()
   window.close()
   
class Tile:
   window = None
   fg_color = pygame.Color("black")
   font_size = 100
   border_width = 10
   image_begin = pygame.image.load('image0.bmp')
   
   def set_window(cls, window):
      #All class methods use cls instead of self. 
      #cls is the CLASS which is calling the method. 
      #in our case, this will always be Tile.
      cls.window = window
   
   
   def __init__(self,x, y, width, height,image):
      self.rect = pygame.Rect(x,y, width, height)
      self.image = image
      self.screen = Tile.window.get_surface()
    
      
   def draw(self):
      pygame.draw.rect(Tile.window.get_surface(), Tile.fg_color, self.rect,Tile.border_width)
      self.screen.blit(image_begin,self.rect)
   
   def select(self,pos):
      if self.rect.collidepoint(self.image,pos):
         if self.screen == 'image0.bmp':
            self.screen.blit(self.image,self.rect)
            return True     
    
              
  
class Game:

   def __init__(self, window):
      self.window = window
      self.pause_time = 0.01
      self.close_clicked = False
      self.continue_game = True
      self.bg_color = pygame.Color('black')
      Tile.set_window(self.window)
      self.image_all = []
      self.load_image()
      self.create_board()
      self.score =0
      self.score_size = 72      
    
   def load_image(self):
      for num in range(1,9):
         image_under = pygame.image.load('image'+str(num)+'.bmp')
         self.image_all.append(image_under)
      self.image_all += self.image_all
      random.shuffle(self.image_all)
      
   def create_board(self):
      self.board = []
      for row_num in range(4):
         new_row = self.create_row(row_num)
         self.board.append(new_row)
      
   def create_row(self,row_num):
      row = [] 
      width = self.window.get_width()/5
      height = self.window.get_height()/4
      for col_num in range(4):
         x = col_num*width
         y = row_num*height
         index = row_num *4 + col_num
         new_tile = Tile(x,y,width,height,self.image_all[index])
         row.append(new_tile)   
      return row
   
   def play(self):
      while not self.close_clicked:
         self.handle_event()
         self.draw()            
         if self.continue_game:
            self.update()
            self.decide_continue()
            time.sleep(self.pause_time) 
          
   def handle_event(self):
      # Handle each user event by changing the game state
      # appropriately.
      # - self is the Game whose events will be handled
      event = pygame.event.poll()
      if event.type == QUIT:
         self.close_clicked = True
                  
         
   def draw(self):
      self.window.clear()
      self.draw_board()
      self.draw_score()
      self.window.update()
      
   def draw_board(self):
      for row in self.board:
         for tile in row:
            tile.draw()
            
   def draw_score(self):
      self.window.set_font_size(self.score_size)
      self.window.draw_string(str(self.score), 435,0)
      
   def update(self):
      self.score = pygame.time.get_ticks() // 1200
      
   def decide_continue(self):    
      if self.is_tie():
         self.continue_game = False
         
   def is_tie(self):
      for row in self.board:
         for tile in row:
            if tile.self.screen =='image0.bmp':
               return False
      return True      
   

main()
