# Written by Rabia Alhaffar in 18/July/2020
# Utilities
import glfw

def get_class(v):
    return (v).__class__.__name__

def get_clipboard_text():
    if not glfw_initialized:
        glfw.init()
    text = glfw.get_clipboard_string(None)
    return text

def set_clipboard_text(text):
    if not glfw_initialized:
        glfw.init()
    glfw.set_clipboard_string(None, text)
    
