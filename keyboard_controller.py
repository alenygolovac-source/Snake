
from pynput import keyboard
# Движение от клавиатури
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
