# Written by Rabia Alhaffar in 18/July/2020
# Physics part,Collision detection engine
from math import sqrt

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

