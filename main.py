
import time
import os
from pynput import keyboard
import random

def check_lose():
    return False

if __name__ == "__main__":
    row = int(input("Enter the row size:"))
    col = int(input("Enter the col size:"))
    dir_snake = "right"
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

    1 - Разбить код на папки и файлы + 
    2 - Загрузить изменение на гит добавив в коммит описания что было сделано с прошлого раза
    3 - Сгенерировать фрукт при создании поля +
    4 - **
        Доработать алгоритм генерации поля
        Который должен ставить # по обводки поля
"""