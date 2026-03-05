
#Движение вправо
def move_right(field, snake_head, snake_body):
    field[snake_head['row']][snake_head['col']] = " "
    snake_head['col'] += 1 
    field[snake_head['row']][snake_head['col']] = "&"
    
    last_body = snake_body.pop()
    snake_body.insert(0,last_body)
    field[snake_body[0]['row']][snake_body[0]['col']] = " "
    snake_body[0]['col'] = snake_head['col'] - 1 
    snake_body[0]['row'] = snake_head['row']
    field[snake_body[0]['row']][snake_body[0]['col']] = "*"
   

#движении влево
def move_left(field, snake_head, snake_body):
    field[snake_head['row']][snake_head['col']] = " "
    snake_head['col'] -= 1 
    field[snake_head['row']][snake_head['col']] = "&"

    last_body = snake_body.pop()
    snake_body.insert(0, last_body)
    field[snake_body[0]['row']][snake_body[0]['col']] = " "
    snake_body[0]['col'] = snake_head['col'] + 1
    snake_body[0]['row'] = snake_head['row']
    field[snake_body[0]['row']][snake_body[0]['col']] = "*"



# движение вниз
def move_down(field, snake_head, snake_body):
    field[snake_head['row']][snake_head['col']] = " "
    snake_head['row'] += 1 
    field[snake_head['row']][snake_head['col']] = "&"

    last_body = snake_body.pop()
    snake_body.insert(0, last_body)

    field[snake_body[0]['row']][snake_body[0]['col']] = " "
    snake_body[0]['row'] = snake_head['row'] - 1 
    snake_body[0]['col'] = snake_head['col']
    field[snake_body[0]['row']][snake_body[0]['col']] = "*"

# движение вверх
def move_up(field,snake_head, snake_body):
    field[snake_head['row']][snake_head['col']] = " "
    snake_head['row'] -= 1 
    field[snake_head['row']][snake_head['col']] = "&"

    last_body = snake_body.pop()
    snake_body.insert(0, last_body)

    field[snake_body[0]['row']][snake_body[0]['col']] = " "
    snake_body[0]['row'] = snake_head['row'] + 1 
    snake_body[0]['col'] = snake_head['col']
    field[snake_body[0]['row']][snake_body[0]['col']] = "*"


def move(dir_snake, field, snake_head, snake_body):
    if dir_snake == "right":
        move_right(field,snake_head, snake_body)
    if dir_snake == "left":
        move_left(field, snake_head, snake_body)
    if dir_snake == "down":
        move_down(field, snake_head, snake_body)
    if dir_snake == "up":
        move_up(field, snake_head, snake_body)