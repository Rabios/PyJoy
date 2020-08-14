# PyJoy lib, Written by Rabia Alhaffar in 19/July/2020

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
from openal import *
from openal.al import *
from openal.alc import *
from os import *
from sys import *
from platform import *
from urllib.parse import urlparse
from zipfile import ZipFile

# Main info
pyjoy_version = "v0.0.3"         # Version
pyjoy_author = "Rabia Alhaffar"  # Author
pyjoy_use_cli = False            # CLI is disabled by default for distributing in games

# Compatibility with Python 2
def xrange(x):
    return range(x)

# CLI
# List of packages used by PyJoy
pyjoy_packages = [
    "PyOpenGL",
    "PyOpenGL_accelerate",
    "PyOpenAL",
    "PyOGG",
    "GLFW",
    "Pillow",
    "freetype-py"
]

if pyjoy_use_cli:
    # Check arguments,If not find folder called "game" and run main.py
    if len(sys.argv) > 1:
        if "-v" in sys.argv or "--version" in sys.argv:
            print(pyjoy_version)
        elif "-p" in sys.argv or "--platform" in sys.argv:
            print(get_os())
        elif "-l" in sys.argv or "--packages" in sys.argv:
            for p in pyjoy_packages:
                print(p)
        elif "test" in sys.argv:
            if os.system("cd sample") == 0:
                os.system("python game\main.py")
        else:
            os.system("python " + (sys.argv[1] + "\main.py"))
    else:
        if os.system("cd game") == 0:
            os.system("python game\main.py")

# Window
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

        if glfw.get_key(self.window, glfw.KEY_ESCAPE):
            glfw.terminate()
            
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
    
# Math
class vec2:
    def __init__(self, x, y):
        self.x = x / 1000
        self.y = y / 1000
        
class vec3:
    def __init__(self, x, y, z):
        self.x = x / 1000
        self.y = y / 1000
        self.z = z / 1000
        
class vec4:
    def __init__(self, x, y, z, w):
        self.x = x / 1000
        self.y = y / 1000
        self.z = z / 1000
        self.w = w / 1000

class quatrenion:
    def __init__(self, a, x, y, z):
        self.a = a / 1000
        self.x = x / 1000
        self.y = y / 1000
        self.z = z / 1000

class color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

class rect:
    def __init__(self, x, y, w, h):
        self.x = x / 1000
        self.y = y / 1000
        self.z = 0
        self.w = w / 1000
        self.h = h / 1000

class circle:
    def __init__(self, x, y, r):
        self.x = x / 1000
        self.y = y / 1000
        self.z = 0
        self.r = r / 1000

class line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1 / 1000
        self.y1 = x1 / 1000
        self.z1 = 0
        self.x2 = x2 / 1000
        self.y2 = y2 / 1000
        self.z2 = 0
        self.w = 1

class triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1 / 1000
        self.y1 = y1 / 1000
        self.z1 = 0
        self.x2 = x2 / 1000
        self.y2 = y2 / 1000
        self.z2 = 0
        self.x3 = x3 / 1000
        self.y3 = y3 / 1000
        self.z3 = 0
    
class polygon:
    def __init__(self, p):
        self.points = p

class cube:
    def __init__(self, x, y, z, s):
        self.x = x / 1000
        self.y = y / 1000
        self.z = z / 1000
        self.s = s / 1000
        self.w = s / 1000
        self.h = s / 1000
        self.l = s / 1000

class cuboid:
    def __init__(self, x, y, z, w, h, l):
        self.x = x / 1000
        self.y = y / 1000
        self.z = z / 1000
        self.w = w / 1000
        self.h = h / 1000
        self.l = l / 1000
        
class sphere:
    def __init__(self, x, y, z, s):
        self.x = x / 1000
        self.y = y / 1000
        self.z = z / 1000
        self.size = s / 1000
        self.slices = 100
        self.stacks = 100

def vec2add(v1, v2):
    return vec2(v1.x + v2.x, v1.y + v2.y)

def vec2sub(v1, v2):
    return vec2(v1.x - v2.x, v1.y - v2.y)

def vec3add(v1, v2):
    return vec3(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z) 

def vec3sub(v1, v2):
    return vec3(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z) 

def vec4add(v1, v2):
    return vec3(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z, v1.w + v2.w) 

def vec4sub(v1, v2):
    return vec3(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z, v1.w - v2.w)

def distance_between(x1, y1, x2, y2):
    return x2 - x1, y2 - y1

def rad2deg(rad):
    return rad * 180 / 3.141592653589793

def deg2rad(deg):
    return deg * 3.141592653589793 / 180

def value(s):
    return s / 1000

# @see https://stackoverflow.com/questions/47896860/how-do-you-apply-textures-with-pyopengl
def generate_cube_vertices(xloc, yloc, zloc, x, y, z):
    x *= 0.5
    y *= 0.5
    z *= 0.5
    vertices = (
        (xloc+x, yloc-y, zloc-z),
        (xloc+x, yloc+y, zloc-z),
        (xloc-x, yloc+y, zloc-z),
        (xloc-x, yloc-y, zloc-z),
        (xloc+x, yloc-y, zloc+z),
        (xloc+x, yloc+y, zloc+z),
        (xloc-x, yloc-y, zloc+z),
        (xloc-x, yloc+y, zloc+z)
    )
    return vertices

# To draw textured cube
cube_surfaces = ((0,1,2,3), (3,2,7,6), (6,7,5,4), (4,5,1,0), (1,5,7,2), (4,0,3,6))

# Physics
def collision_rect(r1, r2):
    return r1.x < r2.x + r2.w and r1.x + r1.w > r2.x and r1.y < r2.y + r2.h and r1.y + r1.h > r2.y

def collision_circle(c1, c2):
    return sqrt((c1.x - c2.x * c1.x - c2.x) + (c1.y + c2.y * c1.y + c2.y)) < c1.r + c2.r

def collision_circle_rect(c, r):
    if abs(c.x - r.x - r.w / 2) > (r.w / 2 + c.r) or abs(c.y - r.y - r.h / 2) > (r.h / 2 + c.r):
        return False
    if abs(c.x - r.x - r.w / 2) <= (r.w / 2) or abs(c.y - r.y - r.h / 2) <= (r.h / 2):
        return True
    return abs(c.x - r.x - r.w / 2) - r.w / 2 * abs(c.x - r.x - r.w / 2) - r.w / 2 + abs(r.y - c.y - r.h / 2) - r.h / 2 * abs(c.y - r.y - r.h / 2) - r.h / 2 <= pow(c.r, 2)
    
def collision_circle_line(c, l):
    dist = 0
    u = ((c.x - l.x1) * (l.x2 - l.x1) + (c.y - l.y1) * (l.y2 - l.y1)) / ((l.y2 - l.y1) * (l.y2 - l.y1) + (l.x2 - l.x1) * (l.x2 - l.x1))
    if u >= 0 and u <= 1:
        dist = pow((l.x1 + (l.x2 - l.x1) * u - c.x), 2) + pow((l.y1 + (l.y2 - l.y1) * u - c.y), 2)
    else:
        if u < 0:
            dist = pow((l.x1 - c.x), 2) + pow((l.y1 - c.y), 2)
        else:
            dist = pow((l.x2 - c.x), 2) + pow((l.y2 - c.y), 2)
    return dist < pow(c.r, 2)


def collision_cube(c1, c2):
    if abs(c1.x - c2.x) < c1.s + c2.s:
        if abs(c1.y - c2.y) < c1.s + c2.s:
            if abs(c1.z - c2.z) < c1.s + c2.s:
                return True
    else:
        return False

def collision_cuboid(c1, c2):
    if abs(c1.x - c2.x) < c1.w + c2.w:
        if abs(c1.y - c2.y) < c1.h + c2.h:
            if abs(c1.z - c2.z) < c1.l + c2.l:
                return True
    else:
        return False

def collision_sphere(s1, s2):
    d = sqrt((s1.x - s2.x) * (s1.x - s2.x) + (s1.y - s2.y) * (s1.y - s2.y) + (s1.z - s2.z) * (s1.z - s2.z))
    return d < (s1.size + s2.size)

def collision_sphere_cube(s, c):

    if abs(s.x - c.x) >= (c.w + s.size):
        return False
    if abs(s.y - c.y) >= (c.h + s.size):
        return False
    if abs(s.z - c.z) >= (c.l + s.size):
        return False

    if abs(s.x - c.x) < c.w:
        return True 
    if abs(s.y - c.y) < c.h:
        return True
    if abs(s.z - c.z) < c.l:
        return True

    d = ((abs(s.x - c.x) - c.w) * (abs(s.x - c.x) - c.w)) + ((abs(s.y - c.y) - c.h) * (abs(s.y - c.y) - c.h)) + ((abs(s.z - c.z) - c.l) * (abs(s.z - c.z) - c.l))

    return d < pow(s.size, 2)

# Audio
# NOTES: OGG and WAV are only supported!
# To manipulate,See link below
# https://github.com/Zuzu-Typ/PyOpenAL#reference-for-pyopenals-own-classes-and-functions

# Deinitialize OpenAL automatically for better control
oalSetAutoInit(False)

class audio:
    def __init__(self, src, audio_type):
        if audio_type == "sound":
            if openal_initialized():
                return oalOpen(src)
        if audio_type == "music":
            if openal_initialized():
                return oalStream(src)

    def playing(self):
        return self.get_state() == AL_PLAYING


def openal_initialized():
    return oalGetInit()

def init_openal():
    if not openal_initialized():
        oalInit()

def close_openal():
    if openal_initialized():
        oalQuit()

def audio_device():
    return oalGetDevice()

def audio_context():
    if openal_initialized():
        return oalGetContext()

# Camera
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

# Input
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

# System
python_version = int(sys.version[0])

def get_os():
    if "win" in sys.platform or sys.platform == "cygwin" or sys.platform == "msys":
        return "Windows"

    elif "darwin" in sys.platform:
        return "Mac"
    
    elif "linux" in sys.platform:
        return "Linux"

    elif "os2" in sys.platform:
        return "OS/2"

    elif "freebsd" in sys.platform:
        return "FreeBSD"

    elif "openbsd" in sys.platform:
        return "OpenBSD"

    else:
        return sys.platform

def execute(cmds):
    return os.system(cmds)

def download(src, dist):
    url = urlparse(src)
    ddist = os.path.basename(url.path)
    if os.system("curl --version") == 0:
        if not os.system("cd %s" % dist) == 0:
            os.system("mkdir %s" % dist)
        os.system("curl -o %s\%s %s" % (dist, os.path.basename(ddist), src))

def extract(src, dist):
    with ZipFile(src, "r") as archive:
        archive.extractall(dist)

def current_directory():
    return os.path.dirname(os.path.realpath(__file__))

def run(python_file):
    os.system("python " + python_file)

# Utilities
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

# Graphics
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
    apply_transforms()
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
    apply_transforms()
    if mode == "fill":
        glBegin(GL_TRIANGLE_FAN)
    if mode == "line":
        glBegin(GL_LINE_LOOP)
    glColor4ub(color.r, color.g, color.b, color.a)
    glVertex3f(circle.x, circle.y, circle.z)
    for angle in range(360):
        glVertex3f(circle.x + sin(angle) * circle.r, circle.y + cos(angle) * circle.r, circle.z)
    glEnd()
        
def draw_triangle(mode, triangle, color):
    glLoadIdentity()
    apply_transforms()
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
    apply_transforms()
    glBegin(GL_LINES)
    glColor4ub(color.r, color.g, color.b, color.a)
    glVertex3f(line.x1, line.y1, line.z1)
    glVertex3f(line.x2, line.y2, line.z2)
    glEnd()

def draw_polygon(mode, polygon, color):
    glLoadIdentity()
    apply_transforms()
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
    apply_transforms()
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
    apply_transforms()
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
    apply_transforms()
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
    apply_transforms()
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
    apply_transforms()
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
    apply_transforms()
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
    apply_transforms()
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
    apply_transforms()
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
    apply_transforms()
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
    apply_transforms()
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
    apply_transforms()
    glPopMatrix()
    reset_transform()
    
def clear_rect(rectangle):
    glEnable(GL_SCISSOR_TEST)
    glScissor(rectangle.x, rectangle.y, rectangle.w, rectangle.h)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)

def translate(x, y, z):
    current_translation.x = x / 1000
    current_translation.y = y / 1000
    current_translation.z = z / 1000
    transform[0] = True
    
def rotate(a, x, y, z):
    current_rotation.a = a
    current_rotation.x = x / 1000
    current_rotation.y = y / 1000
    current_rotation.z = z / 1000
    transform[1] = True

def scale(x, y, z):
    current_scale.x = x / 1000
    current_scale.y = y / 1000
    current_scale.z = z / 1000
    transform[2] = True

def apply_transforms():
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
