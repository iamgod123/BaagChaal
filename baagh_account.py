import numpy as np

from board import Game_Board


class Tiger_Hisab(Game_Board):
    def __init__(self,instance) -> None:
        super().__init__()
        self.blocked_tiger=0
        self.instance=instance
        
    

    
    
    def available_spaces_filtering_blocks(self,row,col):
        
        board=self.instance.get_board()
        block_filtered_spaces=[]
        
        moves=self.instance.available_moves(row,col)
        
        
        
        for x in moves:
                
                r,c=x
                if board[r,c]==0:
                  block_filtered_spaces.append((r,c))

        
        
        
        for x in self.jana_sakne_thau_with_kills(row,col):
                block_filtered_spaces.append(x)
            
        
        array=np.array(block_filtered_spaces)
        print("Available Moves: ")
        print (array)    
        return (array)       
                
    
    def jana_sakne_thau_with_kills(self,row,col):
        
        board=self.instance.get_board()
        available=[]
        bakhra_in_vicinity=[]
        jana_sakne_thau=[]
        position=np.array([row,col])
        
        moves=self.instance.available_moves(row,col)
        for x in moves:

            
                
            r,c=x
            
            
            if board[r,c]==2:
                bakhra_in_vicinity.append((r,c))
        
            
        
        for x in bakhra_in_vicinity:
             
             r,c=x
             
             a=r-row
             b=c-col
             
             
             vec=np.array([a,b])
             
             
             disp_array=2*vec
             
             
             jana_sakne_thau=position+disp_array
             
             
                
                
             if board[(jana_sakne_thau[0]),(jana_sakne_thau[1])]==0:

                        
                        
                        available.append(jana_sakne_thau)
             else:
                        print("marna sakinna")
        

        
        list_version=[tuple(x) for x in available]
        
        
        return (list_version)        
                            
                                
        
    def location_account(self):
        board=self.instance.get_board()
        indices=np.where(board==1)
        list=np.array(indices).T
        reshaped_arr = list.reshape(-1, 2)
        return reshaped_arr
    

    def check_for_blocks(self):
        locations=self.location_account()
        for x in locations:
            available_moves=self.available_spaces_filtering_blocks(x[0],x[1])
            if len(available_moves)==0:
                self.blocked_tiger+=1

    
    def check_bagh_exists(self,row,col):
        board=self.instance.get_board()
        return board[row,col]==1
    
    
