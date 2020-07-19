# Written by Rabia Alhaffar in 18/July/2020
# PyJoy input part
import glfw

mouse_x = 0
mouse_y = 0

def key_down(w, k):
    return glfw.get_key(w.window, k) == glfw.PRESS

def key_up(w, k):
    return glfw.get_key(w.window, k) == glfw.RELEASE

def mouse_down(w, b):
    return glfw.get_mouse_button(w.window, b) == glfw.PRESS

def mouse_up(w, b):
    return glfw.get_mouse_button(w.window, b) == glfw.RELEASE

def mouse_pos(w):
    glfw.get_cursor_pos(w.window, mouse_x, mouse_y)
    return mouse_x, mouse_y

def gamepad_available(i):
    return glfw.joystick_present(i) == glfw.TRUE and glfw.joystick_is_gamepad(i)

def gamepad_button_down(i, b):
    gamepad_state = 0
    if gamepad_available(i):
        if glfw.get_gamepad_state(i, gamepad_state):
            return gamepad_state.buttons[b]
    
def gamepad_name(i):
    if gamepad_available(i):
        return glfw.get_gamepad_name(i)
    
