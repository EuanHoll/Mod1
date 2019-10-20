from OpenGL.GL import *
from OpenGL.GLU import *

class Map:
    def __init__(self, width, height, array):
        self.width = width
        self.height = height
        self.array = array

class Map_3d:
    def __init__(self, verts, edges, width, height):
        self.verts = verts
        self.edges = edges
        self.width = width
        self.height = height

    def draw_map(self):
        glBegin(GL_QUADS)
        y = 1
        while y < self.height:
            x = 0
            while x < self.width - 1:
                i = (y * self.width) + x
                glVertex3fv(self.verts[i - self.width])
                glVertex3fv(self.verts[i - self.width + 1])
                glVertex3fv(self.verts[i + 1])
                glVertex3fv(self.verts[i])
                x += 1
            y += 1
        glEnd()
