# Written by Rabia Alhaffar in 18/July/2020
# PyJoy math part,Contains classes used by various functions
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

class quaternion:
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
