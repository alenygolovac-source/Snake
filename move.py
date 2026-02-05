
#Движение вправо
def move_right(field, snake):
    field[snake['row']][snake['col']] = "."
    snake['col'] += 1 
    field[snake['row']][snake['col']] = "&"

#движении влево
def move_left(field, snake):
    field[snake['row']][snake['col']] = "."
    snake['col'] -= 1 
    field[snake['row']][snake['col']] = "&"

# движение вниз
def move_down(field, snake):
    field[snake['row']][snake['col']] = "."
    snake['row'] += 1 
    field[snake['row']][snake['col']] = "&"

# движение вверх
def move_up(field,snake):
    field[snake['row']][snake['col']] = "."
    snake['row'] -= 1 
    field[snake['row']][snake['col']] = "&"

def move(dir_snake, field, snake):
    if dir_snake == "right":
        move_right(field,snake)
    if dir_snake == "left":
        move_left(field, snake)
    if dir_snake == "down":
        move_down(field, snake)
    if dir_snake == "up":
        move_up(field, snake)