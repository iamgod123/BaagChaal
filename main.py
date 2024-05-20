import numpy as np

from board import Game_Board
from bakhra_account import Goat_Hisab
from baagh_account import Tiger_Hisab
from board_update import update_board

base=Game_Board()
bakhra=Goat_Hisab(base)
baagh=Tiger_Hisab(base)
update=update_board(base)
game_over=False
turn=0


while not game_over:
        
        
        success=False
        if turn == 0:
              
              print(base.get_board())
              print()
              print("Bakhra ko Paalo")
              print()

              if bakhra.bakhra_on_hand!=0:
                  
                print("Where DO YOU WANT TO DROP The PIECE???")
                
                    
                while success==False:
                        
                        r_bakhra_to_place=int(input("Row to place bakhra (0-4): "))
                        
                        c_bakhra_to_place=int(input("Column to place bakhra (0-4): "))
                        
                        success=update.placement(r_bakhra_to_place, c_bakhra_to_place)
                        
                bakhra.placement_ko_account()
                         
                
                

              if bakhra.bakhra_on_hand==0:

                while success==False:
                    r_bakhra_to_move=int(input("Row location of Bakhra(0-4): "))
                    c_bakhra_to_move=int(input("Column location of Bakhra (0-4): "))
                    if bakhra.check_if_bakhra_exists(r_bakhra_to_move,c_bakhra_to_move):
                      
                      print()
                      
                      print()
                      r_bakhra_destination=int(input("Row destination of Bakhra (0-4): "))
                      c_bakhra_destination=int(input("Column Destination of Bakhra (0-4): "))
                      
                      print(bakhra.available_spaces_filtering_blocks(True, False, r_bakhra_to_move,c_bakhra_to_move,r_bakhra_destination,c_bakhra_destination))
                      if base.available_spaces_filtering_blocks(True, False, r_bakhra_to_move,c_bakhra_to_move,r_bakhra_destination,c_bakhra_destination)==True:
                      
                        success=base.Bakhra_movement(r_bakhra_to_move,c_bakhra_to_move,r_bakhra_destination,c_bakhra_destination)
                        
                      else:
                        success=False
                        print("Invalid")
                        print(base.get_board())
                        
                    else:
                        print("Bakhrai chhaina")

               
        else:
              
              print()
              print(base.get_board())
              print()
              
              print("Baagh ko Paalo")

              while success==False:
                    
                print("Locations of Baagh", baagh.location_account())
                r_baagh_to_move=int(input("Row location of Baagh (0-4): "))
                c_baagh_to_move=int(input("Column location of Baagh (0-4): "))
                print()
                
                if baagh.check_bagh_exists(r_baagh_to_move,c_baagh_to_move):

                  position=np.array([r_baagh_to_move,c_baagh_to_move])  
                  possible_movements=baagh.available_spaces_filtering_blocks(r_baagh_to_move,c_baagh_to_move)
                  possible_kills=baagh.jana_sakne_thau_with_kills(r_baagh_to_move,c_baagh_to_move)
                  
                  r_baagh_destination=int(input("Row destination of Baagh (0-4): "))
                  c_baagh_destination=int(input("Column Destination of Baagh (0-4): "))
                  
                      
                
                prospective_destination=np.array([r_baagh_destination, c_baagh_destination])
                if any((prospective_destination==row).all() for  row in possible_movements):
                    success=update.baagh_movement(r_baagh_to_move,c_baagh_to_move,r_baagh_destination,c_baagh_destination)
                    if any((prospective_destination==row).all() for  row in possible_kills):
                        update.baakhra_maryo(position[0],position[1],prospective_destination[0],prospective_destination[1])
                        bakhra.kill_ko_account()
                else:
                    print("No Baagh Exists")
                  
                  
                
                
                
              print("Total Bakhra on Board: ", bakhra.bakhra_on_board)
              print("Total Bakhra Dead: ", bakhra.dead_bakhra())
              print("Total Bakhra on Hand: ",bakhra.bakhra_on_hand)
              print("Locations: ", bakhra.location_account()) 
              print()
              print("Total Baagh blocked: ")
              print("Baagh Locations: ", baagh.location_account())

              
        if bakhra.dead_bakhra==20:
          game_over=True
          print("Baagh Wins")
        if baagh.blocked_tiger==4:
            game_over=True
            print("Bakhra Wins")
        print()
        turn+=1
        turn=turn%2