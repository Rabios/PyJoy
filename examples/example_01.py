# To install PyJoy:
# 1- Copy pyjoy.py from build folder to folder Lib in Python installation folder
# 2- Plus copy again to Python installation folder beside Python compiler binaries

from pyjoy import *

w = window(800, 600, "MYGAME", False)
r = rect(0.0, 0.0, 100 / 1000, 100 / 1000)
while not w.should_close():
    clear(None)
    draw_rect("fill", r, color(0, 0, 255, 255))
    if key_down(w, glfw.KEY_W):
        r.y += 0.001
    if key_down(w, glfw.KEY_S):
        r.y -= 0.001
    if key_down(w, glfw.KEY_A):
        r.x -= 0.001
    if key_down(w, glfw.KEY_D):
        r.x += 0.001
    w.update()
    
