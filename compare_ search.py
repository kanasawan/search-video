import pyglet
import random

window = pyglet.window.Window(width=1000, height=800, caption='Search Algorithms Comparison')
batch = pyglet.graphics.Batch()

def reset_searches():
    global numbers, linear_index, linear_found, binary_left, binary_right, binary_mid, binary_found
    numbers = random.sample(range(1, 50), 21) + [31]
    random.shuffle(numbers)  
    numbers.sort()  

    linear_index = 0
    linear_found = False
    binary_left, binary_right = 0, len(numbers) - 1
    binary_mid = (binary_left + binary_right) // 2
    binary_found = False

reset_searches()  

def update_searches(dt):
    global linear_index, linear_found, binary_left, binary_right, binary_mid, binary_found

     
    if not linear_found and linear_index < len(numbers):
        if numbers[linear_index] == 31:
            linear_found = True
        linear_index += 1


    if not binary_found and binary_left <= binary_right:
        binary_mid = (binary_left + binary_right) // 2
        if numbers[binary_mid] == 31:
            binary_found = True
        elif numbers[binary_mid] < 31:
            binary_left = binary_mid + 1
        else:
            binary_right = binary_mid - 1

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.W:
        reset_searches()

pyglet.clock.schedule_interval(update_searches, 0.5)

@window.event
def on_draw():
    window.clear()
    draw_boxes_and_numbers()

def draw_boxes_and_numbers():
    margin = 5  
    box_size = (window.width - margin * (len(numbers) + 1)) // len(numbers)  
    for i, number in enumerate(numbers):
        x = i * (box_size + margin) + margin  

        y_linear = window.height * 3/4 - box_size / 2
        color_linear = get_box_color_linear(i)
        draw_rectangle(x, y_linear, box_size, color_linear)

        y_binary = window.height / 4 - box_size / 2
        color_binary = get_box_color_binary(i)
        draw_rectangle(x, y_binary, box_size, color_binary)

        draw_label(str(number), x + box_size/2, y_linear + box_size/2)
        draw_label(str(number), x + box_size/2, y_binary + box_size/2)

def draw_rectangle(x, y, size, color):
    pyglet.shapes.Rectangle(x, y, size, size, color=color, batch=batch).draw()

def draw_label(text, x, y):
    label = pyglet.text.Label(text, x=x, y=y, anchor_x='center', anchor_y='center', color=(255, 255, 255, 255), batch=batch)
    label.draw()

def get_box_color_linear(i):
    return (255, 0, 255, 255) if linear_found and i == linear_index - 1 else (255, 165, 0, 255)  if i == linear_index else  (128, 128, 128, 255) 

def get_box_color_binary(i):
    return (255, 0, 255, 255)  if binary_found and i == binary_mid else (255, 165, 0, 255)  if binary_left <= i <= binary_right else  (128, 128, 128, 255) 

pyglet.app.run()