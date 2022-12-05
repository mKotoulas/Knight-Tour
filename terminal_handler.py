from os import system,get_terminal_size
from time import sleep 

def get_terminal_settings():
    rows,columns=get_terminal_size() 
    return rows  

TERMINAL_COLUMNS=get_terminal_settings() #save the user's terminal column setting to restore it later 

def change_terminal_height():
    system('mode con:lines=100')   
    sleep(1) 

def restore_terminal():
    system(f'mode con:lines={TERMINAL_COLUMNS}') 
    #system('CLS') 