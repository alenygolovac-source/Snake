
#Генерация поля
def generate_field(size_r,size_c):
    field = []
    row = []
    for symb in range(1, size_r * size_c + 1):
        row.append('.')
        if symb % size_c == 0:
            field.append(row)
            row = []
    idx1 = random.randint(0, size_r)
    idx2 = random.randint(0, size_c)
    field[idx1][idx2] = "F"
    return field

# Отображение матрицы
def show_field(field):
    for row in field:
        for col in row:
            print(col, end=" ")
        print()

def check_lose():
    return False