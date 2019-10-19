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
        for edge in self.edges:
            for vert in edge:
                glVertex3fv(self.verts[vert])
        glEnd()
