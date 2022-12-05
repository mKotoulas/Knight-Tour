from printings import memo,print_board,print_info,clear_screen 
from random import randint 

def get_random_starting_pos():return [randint(0,7),randint(0,7)]  

def get_random_move_type():return randint(0,7) 

def starting_position(): 
    while True:
        try:
            c_row=int(input("Starting row(0-7):"))   
            c_col=int(input("Starting column(0-7):"))
            if ( c_row<0 or c_col<0 ) or ( c_row>7 or c_col>7):            
                print("Invalid input")     
                continue
            clear_screen()  
            return [c_row,c_col]
        except ValueError:print("Invalid input")

def init_board(row,col,chess_board,visuals=True):
    if visuals:
        chess_board[row][col]=u'♞' 
    else:
        chess_board[row][col]=1
    return chess_board      
 
def update_positions(c_row,c_col,move,h,v):return [c_row+v[move],c_col+h[move]]     

def update_board(chess_board,c_row,c_col,h,v,move_type,number=-1,visuals=True):   
    #single player mode
    if visuals:  
        chess_board[c_row][c_col]='L'   
        c_row,c_col=update_positions(c_row,c_col,move_type,h,v) 
        chess_board[c_row][c_col]=u'♞'
        return chess_board
    #computer solution mode
    c_row,c_col=update_positions(c_row,c_col,move_type,h,v)
    chess_board[c_row][c_col]=number
    return chess_board

def get_move_type(): 
    while True:
        try:
            move=int(input("Move type(0-7)|(-1 for exit):"))
            if move==-1:return move  
            if move<0 or move>7:
                print("Invalid move type!") 
                continue
            return move 
        except ValueError:print("Invalid move type!")
    
def place_x(chess_board,row,col):
    chess_board[row][col]='X' 
    return chess_board  

def restore_board(r,c,chess_board,n):
    chess_board[r][c]=n  
    return chess_board 

def valid_move(c_row,c_col,chess_board,h,v,move_type,visuals=True):   
    new_row=c_row+v[move_type]
    new_col=c_col+h[move_type]
    if ( new_row<0 or new_col<0 ) or ( new_row>7 or new_col>7):
        if visuals:print("Leaving the battlefield is not really an option!")   
        return False 
    if chess_board[new_row][new_col]!=0: 
        if visuals:print("You were already there!") 
        return False 
    return True  

def knight_trapped(chess_board,c_row,c_col,h,v):   
    for move in range(8):
        if valid_move(c_row,c_col,chess_board,h,v,move,visuals=False):return False      
    return True

def init_game(chess_board,visuals=True): 
    #computer solution mode 
    if not visuals: 
        c_row,c_col=get_random_starting_pos()
        chess_board=init_board(c_row,c_col,chess_board,visuals)    
        return [c_row,c_col,chess_board]  
    #single-player mode
    c_row,c_col=starting_position() 
    chess_board=init_board(c_row,c_col,chess_board) 
    memo()
    print_info()
    print(f"     Progress:1/64\n")    
    print_board(chess_board)   
    return [c_row,c_col,chess_board]