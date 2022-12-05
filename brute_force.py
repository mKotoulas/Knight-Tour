from utils import * 

def brute_force():
    clear_screen()     
    horizontal=[2,1,-1,-2,-2,-1,1,2] #Seems like that and the horizontal array should be global variables among files.
    vertical=[-1,-2,-2,-1,1,2,2,1]    
    success=False
    moves_made=1
    while not success:
        print(moves_made)
        chessboard=[[0 for _ in range(8)] for _ in range(8)]   
        moves_made=1 
        c_row,c_col,chessboard=init_game(chessboard,visuals=False)#start a new board with a new random starting position   
        while not knight_trapped(chessboard,c_row,c_col,horizontal,vertical):
            move_type=get_random_move_type()
            if valid_move(c_row,c_col,chessboard,horizontal,vertical,move_type,visuals=False): 
                moves_made+=1
                chessboard=update_board(chessboard,c_row,c_col,horizontal,vertical,move_type,moves_made,visuals=False) 
                c_row,c_col=update_positions(c_row,c_col,move_type,horizontal,vertical)  
                if moves_made==64:success=True

    print("A solution is found!\n")  
    print_board(chessboard)
    input("Type anything to return to menu:")   













