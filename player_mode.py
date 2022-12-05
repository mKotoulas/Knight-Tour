from utils import *
from printings import clear_screen

def single_player():
    clear_screen() 
    chessboard=[[0 for _ in range(8)] for _ in range(8)]    
    horizontal=[2,1,-1,-2,-2,-1,1,2]
    vertical=[-1,-2,-2,-1,1,2,2,1]  
    moves_made=1 

    c_row,c_col,chessboard=init_game(chessboard)    
    move_type=0 #just a random value that is not -1 to make the loop run at least one time. Not the best practice,probably  
    while move_type!=-1: 
        if moves_made==64:
            print('Success!')  
            break
        if knight_trapped(chessboard,c_row,c_col,horizontal,vertical):     
            print("\nOut of moves...") 
            break 
        move_type=get_move_type()
        if valid_move(c_row,c_col,chessboard,horizontal,vertical,move_type):  
            clear_screen()
            chessboard=update_board(chessboard,c_row,c_col,horizontal,vertical,move_type)
            l_row,l_col=c_row,c_col
            c_row,c_col=update_positions(c_row,c_col,move_type,horizontal,vertical)      
            memo() 
            print_info()
            print(f"     Progress:{moves_made+1}/64\n")
            print_board(chessboard)
            chessboard=place_x(chessboard,l_row,l_col)     
            moves_made+=1 
    input("Type anything to return to menu:")      
     



