
import random
#Генерация поля
def generate_field(size_r,size_c, snake_head, snake_body):
    field = []
    row = []
    for symb in range(1, size_r * size_c + 1):
        if len(field) == 0: 
            row.append('#')
        elif len(field) == size_r - 1:
            row.append('#')
        else:
            row.append(' ')
        if symb % size_c == 0:
            row[0] = "#"
            row[size_c -1] = "#" 
            field.append(row)
            row = []
    field[snake_head["row"]][snake_head["col"]] = "&"
    for body in snake_body:
        field[body["row"]][body["col"]] = "*"
    return field

#Генерация фрукта
def generate_fruit(field, size_r, size_c):
    fruit_row = random.randint(1, size_r - 2)
    fruit_col = random.randint(1, size_c - 2)
    field[fruit_row][fruit_col] = "F"
    return {'row':fruit_row,'col':fruit_col}