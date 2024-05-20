import numpy as np

from board import Game_Board


class Goat_Hisab(Game_Board):
    
    def __init__(self,instance):
        super().__init__()
        self.instance=instance
        self.bakhra_on_hand=20
        self.bakhra_on_board=0

    def dead_bakhra(self):
        return (20-self.bakhra_on_hand-self.bakhra_on_board)    

    def placement_ko_account(self):
        self.bakhra_on_board+=1
        self.bakhra_on_hand-=1
        pass
    
    def location_account(self):
        board=self.instance.get_board()
        indices=np.where(board==2)
        list=np.array(indices)
        reshaped_arr = list.reshape(-1, 2)
        return reshaped_arr


    def kill_ko_account(self):
        self.bakhra_on_board-=1
        pass

    def available_spaces_filtering_blocks(self,row,col):
        
        board=self.instance.get_board()
        block_filtered_spaces=[]
        
        moves=self.available_moves(row,col)
        
        for x in moves:
                
                r=x[0]
                c=x[1]
                
                if board[r,c]==0:
                  block_filtered_spaces.append(x)
        return np.array(block_filtered_spaces)      

    def check_if_bakhra_exists(self,row,column):
        return self.board[row,column]==2         
            
