
import time
import os
#from keyboard_controller import on_press
from pynput import keyboard

from move import *
from interface import *

def check_lose():
    return False

def on_press(key):
    global dir_snake
    print(key, "==", keyboard.Key.left)
    if key == keyboard.Key.right:
        dir_snake = "right"
    elif key == keyboard.Key.left:
        dir_snake = "left"
        print(dir_snake)
    elif key == keyboard.Key.down:
        dir_snake = "down"
    elif key == keyboard.Key.up:
        dir_snake = "up"

dir_snake = "right"

if __name__ == "__main__":
    row = int(input("Enter the row size:"))
    col = int(input("Enter the col size:"))
    field = generate_field(row,col)
    snake = {"row": int(row/2), "col": int(col/2)}
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while True:
        os.system("clear")
        move(dir_snake, field, snake)
        show_field(field)
        result = check_lose()
        if result == True:
            break
        time.sleep(1)


"""
    1 - Генерацию фрукта вынести в функцию 
    2 - *
        Если мы скушали фрукт вывести в консоль информацию об этом
    3 - **
        Доработать рисование границы
"""