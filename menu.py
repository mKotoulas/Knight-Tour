#import terminal_handler as tm
from printings import menu_text,clear_screen
from player_mode import single_player
from brute_force import brute_force 
from sys import exit  

MENU_FUNCTIONS={"1":single_player,"2":brute_force,"3":exit}

while True:
    clear_screen() 
    menu_text()
    choice=input("Select your choice:") 
    MENU_FUNCTIONS[choice]() 

#tm.change_terminal_height()  