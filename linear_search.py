import pyglet
import random


window = pyglet.window.Window(width=800, height=200, caption='Linear Search')
batch = pyglet.graphics.Batch()

existing_numbers = set(random.sample(range(1, 50), 21) + [31])
numbers = list(existing_numbers)
random.shuffle(numbers)  


current_index = 0
found_index = -1
search_complete = False

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == 31:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True


pyglet.clock.schedule_interval(lambda dt: linear_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        
        if i == current_index and not search_complete:
            color = hex_to_rgb('#AF9F8C')  # Sand
        elif i == found_index:
            color = hex_to_rgb('#7F867B') # Green 
        else:
            color = hex_to_rgb('#AA7C7A')# Grey 
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()
