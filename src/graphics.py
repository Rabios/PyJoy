# Written by Rabia Alhaffar in 19/July/2020
# PyJoy graphics part,Uses OpenGL Desktop

import glfw
import numpy
import OpenGL
OpenGL.ERROR_LOGGING = True
from OpenGL.GL import *
from OpenGL.GLE import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from math import *
from freetype import *

current_translation = vec3(0.0, 0.0, 0.0)
current_rotation = quatrenion(0, 0.0, 0.0, 0.0)
current_scale = vec3(0.0, 0.0, 0.0)
transform = [ False, False, False ]

class texture:
    def __init__(self, id, src, rect):
        self.id = id
        self.src = src
        self.x = rect.x
        self.y = rect.y
        self.z = rect.z
        self.w = rect.w
        self.h = rect.h

def reset_transform():
    current_scale.x = 0.0
    current_scale.y = 0.0
    current_scale.z = 0.0
    current_translation.x = 0.0
    current_translation.y = 0.0
    current_translation.z = 0.0
    current_rotation.a = 0
    current_rotation.x = 0.0
    current_rotation.y = 0.0
    current_rotation.z = 0.0

def clear(color):
    if not color == None:
        glClearColor(color.r, color.g, color.b, color.a)
    else:
        glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
def draw_rect(mode, rect, color):
    glLoadIdentity()
    apply()
    if mode == "fill":
        glBegin(GL_QUADS)
    if mode == "line":
        glBegin(GL_LINE_LOOP)
    glColor4ub(color.r, color.g, color.b, color.a)
    glVertex3f(rect.x, rect.y, rect.z)
    glVertex3f(rect.x + rect.w, rect.y, rect.z)
    glVertex3f(rect.x + rect.w, rect.y + rect.h, rect.z)
    glVertex3f(rect.x, rect.y + rect.h, rect.z)
    glEnd()

def draw_circle(mode, circle, color):
    glLoadIdentity()
    apply()
    if mode == "fill":
        glBegin(GL_TRIANGLE_FAN)
    if mode == "line":
        glBegin(GL_LINE_LOOP)
    glColor4ub(color.r, color.g, color.b, color.a)
    glVertex3f(circle.x, circle.y, circle.z)
    for angle in range(360):
        glVertex3f(circle.x + math.sin(angle) * circle.r, y + math.cos(angle) * circle.r, circle.z)
    glEnd()
        
def draw_triangle(mode, triangle, color):
    glLoadIdentity()
    apply()
    if mode == "fill":
        glBegin(GL_TRIANGLES)
    if mode == "line":
        glBegin(GL_LINE_LOOP)
    glColor4ub(color.r, color.g, color.b, color.a)
    glVertex3f(triangle.x1, triangle.y1, triangle.z1)
    glVertex3f(triangle.x2, triangle.y2, triangle.z2)
    glVertex3f(triangle.x3, triangle.y3, triangle.z3)
    glEnd()

def draw_line(line, color):
    glPointSize(line.w)
    glLoadIdentity()
    apply()
    glBegin(GL_LINES)
    glColor4ub(color.r, color.g, color.b, color.a)
    glVertex3f(line.x1, line.y1, line.z1)
    glVertex3f(line.x2, line.y2, line.z2)
    glEnd()

def draw_polygon(mode, polygon, color):
    glLoadIdentity()
    apply()
    if mode == "fill":
        glBegin(GL_POLYGON)
    if mode == "line":
        glBegin(GL_LINE_LOOP)
    glColor4ub(color.r, color.g, color.b, color.a)
    for p in polygon.points:
        glVertex3f(polygon.points[p].x, polygon.points[p].y, polygon.points[p].z)
    glEnd()

def draw_text(mode, text, x, y, z, color):
    glLoadIdentity()
    apply()
    glColor4ub(color.r, color.g, color.b, color.a)
    if mode == "line":
        glRasterPos3i(x, y, z)
        glutStrokeString(GLUT_BITMAP_HELVETICA_18, text)
    if mode == "fill":
        glRasterPos3i(x, y, z)
        glutBitmapString(GLUT_BITMAP_HELVETICA_18, text)

def draw_texture(src, x, y, w, h):
    img = Image.open(src)
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glEnable(GL_DEPTH)
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,w,h,GL_UNSIGNED_BYTE,GL_RGB,0, texture)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR) 
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S,GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,GL_CLAMP)
    glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA)
    glLoadIdentity()
    glPushMatrix()
    apply()
    glBegin(GL_QUADS)
    glTexCoord2d(0, 0)
    glVertex3f(x, y, z)
    glTexCoord2d(1,0)
    glVertex3f(x + w, y, z)
    glTexCoord2d(1,1)
    glVertex3f(x + w, y - h, z)
    glTexCoord2d(0,1)
    glVertex3f(x, y - h, z)
    glEnd()
    glPopMatrix()
    reset_transform()
    glDisable(GL_TEXTURE_2D)
    glDeleteTexture(texture)

def draw_cube(mode, cube, color):
    glLoadIdentity()
    glPushMatrix()
    glColor4ub(color.r, color.g, color.b, color.a)
    glTranslatef(cube.x, cube.y, cube.z)
    if mode == "fill":
        glutSolidCube(c.s)
    if mode == "line":
        glutWireCube(c.s)
    apply()
    glPopMatrix()
    reset_transform()

def draw_textured_cube(cube, size):
    img = Image.open(src)
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glEnable(GL_DEPTH)
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,w,h,GL_UNSIGNED_BYTE,GL_RGB,0, texture)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR) 
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S,GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,GL_CLAMP)
    glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA)
    glLoadIdentity()
    apply()
    for surface in cube_surfaces:
        n = 0
        glBegin(GL_QUADS)
        for vertex in surface:
            if n == 0:
                xv = 0.0
                yv = 0.0
            if n == 1:
                xv = 1.0
                yv = 0.0
            if n == 2:
                xv = 1.0
                yv = 1.0
            if n == 3:
                xv = 0.0
                yv = 1.0
            glTexCoord2f(xv,yv)
            glVertex3fv(generate_cube_vertices(xloc,yloc,zloc,x,y,z)[vertex])
            n += 1
        glEnd()
    reset_transform()
    glDisable(GL_TEXTURE_2D)
    glDeleteTexture(texture)
    

def draw_sphere(mode, sphere, color):
    glLoadIdentity()
    glPushMatrix()
    glColor4ub(color.r, color.g, color.b, color.a)
    glTranslatef(s.x, s.y, s.z)
    if mode == "fill":
        glutSolidSphere(s.size, s.slices, s.stacks)
    if mode == "line":
        glutWireSphere(s.size, s.slices, s.stacks)
    apply()
    glPopMatrix()
    reset_transform()

def draw_cone(mode, pos, radius, height, slices, stacks, color):
    glLoadIdentity()
    glPushMatrix()
    glColor4ub(color.r, color.g, color.b, color.a)
    glTranslatef(pos.x, pos.y, pos.z)
    if mode == "fill":
        glutSolidCone(radius, height, slices, stacks)
    if mode == "line":
        glutWireCone(radius, height, slices, stacks)
    apply()
    glPopMatrix()
    reset_transform()
    
def draw_torus(mode, pos, inner_radius, outer_radius, sides, rings, color):
    glLoadIdentity()
    glPushMatrix()
    glColor4ub(color.r, color.g, color.b, color.a)
    glTranslatef(pos.x, pos.y, pos.z)
    if mode == "fill":
        glutSolidTorus(inner_radius, outer_radius, sides, rings)
    if mode == "line":
        glutWireTorus(inner_radius, outer_radius, sides, rings)
    apply()
    glPopMatrix()
    reset_transform()

def draw_icosahedron(mode, pos, color):
    glLoadIdentity()
    glPushMatrix()
    glColor4ub(color.r, color.g, color.b, color.a)
    glTranslatef(pos.x, pos.y, pos.z)
    if mode == "fill":
        glutSolidIcosahedron()
    if mode == "line":
        glutWireIcosahedron()
    apply()
    glPopMatrix()
    reset_transform()

def draw_dodecahedron(mode, pos, color):
    glLoadIdentity()
    glPushMatrix()
    glColor4ub(color.r, color.g, color.b, color.a)
    glTranslatef(pos.x, pos.y, pos.z)
    if mode == "fill":
        glutSolidDodecahedron()
    if mode == "line":
        glutWireDodecahedron()
    apply()
    glPopMatrix()
    reset_transform()

def draw_octahedron(mode, pos, color):
    glLoadIdentity()
    glPushMatrix()
    glColor4ub(color.r, color.g, color.b, color.a)
    glTranslatef(pos.x, pos.y, pos.z)
    if mode == "fill":
        glutSolidOctahedron()
    if mode == "line":
        glutWireOctahedron()
    apply()
    glPopMatrix()
    reset_transform()

def draw_octahedron(mode, pos, color):
    glLoadIdentity()
    glPushMatrix()
    glColor4ub(color.r, color.g, color.b, color.a)
    glTranslatef(pos.x, pos.y, pos.z)
    if mode == "fill":
        glutSolidOctahedron()
    if mode == "line":
        glutWireOctahedron()
    apply()
    glPopMatrix()
    reset_transform()
    
def clear_rect(rectangle):
    glEnable(GL_SCISSOR_TEST)
    glScissor(rectangle.x, rectangle.y, rectangle.w, rectangle.h)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)

def translate(x, y, z):
    current_translation.x = x
    current_translation.y = y
    current_translation.z = z
    transform[0] = True
    
def rotate(a, x, y, z):
    current_rotation.a = a
    current_rotation.x = x
    current_rotation.y = y
    current_rotation.z = z
    transform[1] = True

def scale(x, y, z):
    current_scale.x = x
    current_scale.y = y
    current_scale.z = z
    transform[2] = True

def apply():
    if transform[0]:
        glTranslate(current_translation.x, current_translation.y, current_translation.z)
        transform[0] = False
    if transform[1]:
        glRotate(current_rotation.a, current_rotation.x, current_rotation.y, current_rotation.z)
        transform[1] = False
    if transform[2]:
        glScale(current_scale.x, current_scale.y, current_scale.z)
        transform[2] = False
        
def save():
    glPushMatrix()

def restore():
    glPopMatrix()

def set_lighting(l):
    if l:
        glEnable(GL_LIGHTING)
    else:
        glDisable(GL_LIGHTING)
