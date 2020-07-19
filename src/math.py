# Written by Rabia Alhaffar in 18/July/2020
# PyJoy math part,Contains classes used by various functions
class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
class vec4:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

class quatrenion:
    def __init__(self, a, x, y, z):
        self.a = a
        self.x = x
        self.y = y
        self.z = z

class color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

class rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.z = 0
        self.w = w
        self.h = h

class circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.z = 0
        self.r = r

class line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = x1
        self.z1 = 0
        self.x2 = x2
        self.y2 = y2
        self.z2 = 0
        self.w = 1

class triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.z1 = 0
        self.x2 = x2
        self.y2 = y2
        self.z2 = 0
        self.x3 = x3
        self.y3 = y3
        self.z3 = 0
    
class polygon:
    def __init__(self, p):
        self.points = p

class cube:
    def __init__(self, x, y, z, s):
        self.x = x
        self.y = y
        self.z = z
        self.s = s
        self.w = s
        self.h = s
        self.l = s

class cuboid:
    def __init__(self, x, y, z, w, h, l):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.h = h
        self.l = l
        
class sphere:
    def __init__(self, x, y, z, s):
        self.x = x
        self.y = y
        self.z = z
        self.size = s
        self.slices = 100
        self.stacks = 100

class line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = 0
        self.x2 = x2
        self.y2 = y2
        self.z2 = 0
        self.width = 1
        
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
