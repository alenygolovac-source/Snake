
from pynput import keyboard
from state_snake import set_dir_snake, get_dir_snake

# Движение от клавиатури
def on_press(key):
    dir_snake = get_dir_snake()
    print(key, "==", keyboard.Key.left)
    if key == keyboard.Key.right and dir_snake != "left":
        set_dir_snake("right")
    elif key == keyboard.Key.left and dir_snake != "right":
        set_dir_snake("left")
    elif key == keyboard.Key.down and dir_snake != "up":
        set_dir_snake("down")
    elif key == keyboard.Key.up and dir_snake != "down":
        set_dir_snake("up")
