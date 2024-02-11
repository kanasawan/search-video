import pyglet
import random

window = pyglet.window.Window(width=800, height=200, caption='Binary Search')
batch = pyglet.graphics.Batch()

existing_numbers = set(random.sample(range(1, 50), 21) + [31])
numbers = sorted(existing_numbers)

left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def binary_search(dt):
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == 31:
            found = True
        elif numbers[mid] < 31:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True

def update(dt):
    binary_search(dt)
    on_draw()

pyglet.clock.schedule_interval(update, 0.5)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        if left <= i <= right and not search_complete:
            color = hex_to_rgb('#AF9F8C')  # Sand
        elif i == mid and not search_complete:
            color = hex_to_rgb('#7F867B')  # Grass 
        elif found and i == mid:
            color = hex_to_rgb('#AA7C7A')  # Rose
        else:
            color = hex_to_rgb('#787A79')  # Charcoal

        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()