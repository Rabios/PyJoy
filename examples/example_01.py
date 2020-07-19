# To install PyJoy:
# 1- Copy pyjoy.py from build folder to folder Lib in Python installation folder.
# 2- Plus copy again to Python installation folder beside Python compiler binaries.
# Then go to tools folder in repo and run install dependencies whatever your Python version.

from pyjoy import *

w = window(800, 600, "MYGAME", False)
r = rect(0.0, 0.0, 100 / 1000, 100 / 1000)
while not w.should_close():
    clear(None)
    draw_rect("fill", r, color(0, 0, 255, 255))
    if key_down(w, glfw.KEY_W):
        r.y += 1 / 1000
    if key_down(w, glfw.KEY_S):
        r.y -= 1 / 1000
    if key_down(w, glfw.KEY_A):
        r.x -= 1 / 1000
    if key_down(w, glfw.KEY_D):
        r.x += 1 / 1000
    w.update()
    
