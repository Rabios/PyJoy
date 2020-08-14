# To install PyJoy:
# 1- Copy pyjoy.py from build folder to folder Lib in Python installation folder.
# 2- Plus copy again to Python installation folder beside Python compiler binaries.
# Then go to tools folder in repo and run install dependencies whatever your Python version.

from pyjoy import *

# Create window
w = window(800, 600, "MYGAME", False)

# Create rectangle class
r = rect(0.0, 0.0, 100 / 1000, 100 / 1000)

while not w.should_close():
    # Clear in black, Or define color
    clear(color(0, 0, 0, 255))
    
    # Draw
    draw_rect("fill", r, color(0, 0, 255, 255))

    # If key down
    if key_down(w, glfw.KEY_W) or key_down(w, glfw.KEY_UP):
        r.y += 1 / 1000
    if key_down(w, glfw.KEY_S) or key_down(w, glfw.KEY_DOWN):
        r.y -= 1 / 1000
    if key_down(w, glfw.KEY_A) or key_down(w, glfw.KEY_LEFT):
        r.x -= 1 / 1000
    if key_down(w, glfw.KEY_D) or key_down(w, glfw.KEY_RIGHT):
        r.x += 1 / 1000

    # Render and update game window
    w.update()
    
close_window()
