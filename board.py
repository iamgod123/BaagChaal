import numpy as np


class Game_Board():
    
    def __init__(self):
        self.board = np.zeros((5, 5))
        self.board[0, 0] = 1
        self.board[4, 0] = 1
        self.board[0, 4] = 1
        self.board[4, 4] = 1
        self.bakhra_on_board=0
    
    def get_board(self):
        return self.board
    
    
    def update(self,array):
        self.board=array

     
    def available_moves(self,row,column):
         av_spaces=[]
         
         for x in (-1,0,1):
              for j in (-1,0,1):
                   if 4>=row+x>=0 and 4>=column+j>=0 and (row+x!=row or column+j!=column):
                    av_spaces.append((row+x,column+j))
        

         items=len(av_spaces)           
         if (row+column)%2!=0:
            to_del=[]
            for x in range(items):
                 
                 if av_spaces[x][0]!=row and av_spaces[x][1]!=column:
                      to_del.append((av_spaces[x][0],av_spaces[x][1]))
             
            final_av_spaces=[x for x in av_spaces if x not in to_del]
                 
         else:
              final_av_spaces=av_spaces             
         
          
         array_of_available_moves=np.array(final_av_spaces)
         
         return(array_of_available_moves)
    
    
    
    
    
    def check_bagh_exists(self,row,col):
        return self.board[row,col]==1
    
    def check_bakhra_exists(self,row,col):
        return self.board[row,col]==2