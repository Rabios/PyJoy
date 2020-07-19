# Written by Rabia Alhaffar in 18/July/2020
# Window manipulation part
import glfw

glfw_initialized = False

class window:
    def __init__(self, w, h, t, f):
        self.width = w
        self.height = h
        self.title = t
        self.fullscreen = f
        self.refresh_rate = 60
        glfw.init()
        if glfw.init() == 1:
            glfw_initialized = True
        if self.fullscreen:
            self.window = glfw.create_window(self.width, self.height, self.title, glfw.get_primary_monitor(), None)
        else:
            self.window = glfw.create_window(self.width, self.height, self.title, None, None)
        if not self.window:
            glfw.terminate()
        self.x, self.y = glfw.get_window_pos(self.window)
        glfw.make_context_current(self.window)
        
    def ready(self):
        return self.window
        
    def should_close(self):
        return glfw.window_should_close(self.window) or glfw.get_key(self.window, glfw.KEY_ESCAPE) == glfw.PRESS
        
    def update(self):
        if self.fullscreen:
            glfw.set_window_monitor(self.window, glfw.get_primary_monitor(), self.x, self.y, self.width, self.height, self.refresh_rate)
        else:
            glfw.set_window_monitor(self.window, None, self.x, self.y, self.width, self.height, self.refresh_rate)
        glfw.swap_buffers(self.window)
        glfw.poll_events()

    def resize(self, w, h):
        if not self.fullscreen:
            glfw.set_window_size(self.window, w, h)

    def set_title(self, t):
        glfw.set_window_title(self.window, t)

def close_window():
    if glfw_initialized:
        glfw.terminate()

def set_refresh_rate(w, r):
    w.refresh_rate = r

def set_fullscreen(w, f):
    w.fullscreen = f
