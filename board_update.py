import numpy as np
from board import Game_Board
from bakhra_account import Goat_Hisab



class update_board(Game_Board):
    
    def __init__(self,instance):
         super().__init__()
         self.instance=instance


    
    def update_board(self,array):
         self.instance.board=array
    
    def baagh_movement(self,r1,c1,r2,c2):
         board=self.instance.get_board()
         board[r1,c1]=0
         board[r2,c2]=1
         self.instance.update(board)
         

    def baakhra_maryo(self,r1,c1,r2,c2):
         board=self.instance.get_board()
         x1=(r1+r2)//2
         y1=(c1+c2)//2
         board[x1,y1]=0            
         self.instance.update(board)       
            
               
         
    
    
    def placement(self,row,column):
      
      board=self.instance.get_board()
      
      if board[row, column] == 0:
            board[row, column] = 2
            self.instance.update(board)
            
            return True
      else:
            print("Unable to place Bakhra")
            return False
    
      
    


