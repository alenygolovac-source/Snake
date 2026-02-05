
import random

#Генерация поля
def generate_field(size_r,size_c):
    field = []
    row = []
    for symb in range(1, size_r * size_c + 1):
        if len(field) == 0: 
            row.append('#')
        elif ...:
            row.append('#')
        else:
            row.append('.')
        if symb % size_c == 0:
            row[0] = "#"
            row[size_c -1] = "#" 
            field.append(row)
            row = []
    idx1 = random.randint(0, size_r)
    idx2 = random.randint(0, size_c)
    field[idx1][idx2] = "F"
    return field

# Отображение поле
def show_field(field):
    for row in field:
        for col in row:
            print(col, end=" ")
        print()


# В ров первый и последний элемент стоят #