

def eating_fruit(snake_head, fruit):
    if snake_head['row'] == fruit['row'] and snake_head['col'] == fruit['col']:
        return True
    return False

    