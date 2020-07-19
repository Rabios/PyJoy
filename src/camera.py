# Written by Rabia Alhaffar in 18/July/2020
# PyJoy camera class
import OpenGL
OpenGL.ERROR_LOGGING = True
from OpenGL.GL import *

graphics_z = -1000.0

# For 2D camera, In rotation camera
class camera:
    def __init__(self, position, rotation, up):
        self.position = position
        self.rotation = rotation
        self.up = up
        self.scale = 0.0
        
    def render(self):
        glLoadIdentity()
        glPushMatrix()
        glRotatef(self.up.x, self.rotation.x, 0.0, 0.0)
        glRotatef(self.up.y, 0.0, self.rotation.y, 0.0)
        glRotatef(self.up.z, 0.0, 0.0, self.rotation.z)
        glTranslatef(self.position.x, self.position.y, self.position.z)
        glScalef(self.scale, self.scale, self.scale)
        glPopMatrix()
    
        
        




