
import time
import os
from keyboard_controller import on_press
from pynput import keyboard
from state_snake import get_dir_snake

from move import *
from interface import *
from generate import *
from game import *

def check_lose(snake_head,snake_body, row,col):
    if snake_head['col'] == col-1 or snake_head['col'] == 0:
        return True
    elif snake_head['row'] == row - 1 or snake_head['row'] == 0:
        return True
    for element_body in snake_body:
        if snake_head['row'] == element_body['row'] and snake_head['col'] == element_body['col']:
            return True
    
    


if __name__ == "__main__":
    row = int(input("Enter the row size:"))
    col = int(input("Enter the col size:"))
    snake_head = {"row": int(row/2), "col": int(col/2)}
    snake_body = [
        {"row": snake_head["row"], "col": snake_head["col"] - 1}, 
        {"row": snake_head["row"], "col": snake_head["col"] - 2}
    ]
    field = generate_field(row,col, snake_head, snake_body)
    fruit = generate_fruit(field, row, col)
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while True:
        os.system("clear")
        show_field(field)
        res_lose = check_lose(snake_head,snake_body,row,col)
        if res_lose == True:
            break
        move(get_dir_snake(), field, snake_head, snake_body)
        res_eat = eating_fruit(snake_head, fruit)
        if res_eat == True:
            snake_body.append({"row": snake_head["row"], "col": snake_head["col"]})
            fruit = generate_fruit(field, row, col)
        time.sleep(1)


"""
    OOP
    Network
    Site / Chat  Bot 
"""