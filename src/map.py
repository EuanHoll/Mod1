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
        glBegin(GL_LINES)
        y = 1
        glColor3f(1, 1, 1)
        while y < self.height:
            x = 0
            while x < self.width - 1:
                i = (y * self.width) + x
                self.draw_trig(self.verts[i - self.width],
                                self.verts[i - self.width + 1],
                                self.verts[i])
                self.draw_trig(self.verts[i - self.width + 1],
                                     self.verts[i + 1],
                                     self.verts[i])
                x += 1
            y += 1
        glEnd()

    def draw_trig(self, vert_1, vert_2, vert_3):
        glVertex3fv(vert_1)
        glVertex3fv(vert_2)
        glVertex3fv(vert_3)
