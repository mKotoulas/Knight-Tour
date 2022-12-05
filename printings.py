from os import system,get_terminal_size  

movement_symbols=["⬏","↱","↰","⬑","⬐","↲","↳","⬎"] 
width=get_terminal_size().columns     

def center(n):
    for _ in range(n):print(" ",end="")   

def memo():
    center(round(0.4*width))
    print("Movements") 
    for i in range(8): 
        center(round(0.4*width)+2) 
        print(f"{movement_symbols[i]} : {i}")
          
def print_info():
    print("----------------INFO----------------") 
    print("0 : A square you haven't visited")  
    print("X : A square you have already visited")
    print("L : Previous position")
    print("♞ : Current Position")
    print("------------------------------------\n") 

def clear_screen():system("cls")

def print_board(chess_board): 
    for row in range(8):
        for col in range(8):
            print(chess_board[row][col],end="")   
            print("  ",end="")
        print() 

def menu_text():
    print("-----------MENU--------------")
    print("1.Attemt a solution mannually")
    print("2.Find a random solution using brute force")
    print("3.Exit")   