from OpenGL.GL import *
from OpenGL.GLU import *
import const as c


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
        glBegin(GL_TRIANGLES)
        y = 1
        while y < self.height:
            x = 0
            while x < self.width - 1:
                i = (y * self.width) + x
                self.draw_trig(self.verts[i],
                               self.verts[i - self.width],
                               self.verts[i - self.width + 1])
                self.draw_trig(self.verts[i],
                               self.verts[i - self.width + 1],
                               self.verts[i + 1])
                #self.draw_lines(self.verts[i],
                #                self.verts[i - self.width],
                #                self.verts[i - self.width + 1],
                #                self.verts[i + 1])
                x += 1
            y += 1
        glEnd()

    def draw_lines(self, vert_1, vert_2, vert_3, vert_4):
        c_1 = self.get_color(vert_1[2])
        c_2 = self.get_color(vert_2[2])
        c_3 = self.get_color(vert_3[2])
        c_4 = self.get_color(vert_4[2])
        glColor3fv(c_1)
        glVertex3fv(vert_1)
        glColor3fv(c_2)
        glVertex3fv(vert_2)
        glColor3fv(c_2)
        glVertex3fv(vert_2)
        glColor3fv(c_3)
        glVertex3fv(vert_3)
        glColor3fv(c_3)
        glVertex3fv(vert_3)
        glColor3fv(c_1)
        glVertex3fv(vert_1)
        glColor3fv(c_1)
        glVertex3fv(vert_1)
        glColor3fv(c_4)
        glVertex3fv(vert_4)
        glColor3fv(c_4)
        glVertex3fv(vert_4)
        glColor3fv(c_3)
        glVertex3fv(vert_3)

    def draw_trig(self, vert_1, vert_2, vert_3):
        glColor3fv(self.get_color(vert_1[2]))
        glVertex3fv(vert_1)
        glColor3fv(self.get_color(vert_2[2]))
        glVertex3fv(vert_2)
        glColor3fv(self.get_color(vert_3[2]))
        glVertex3fv(vert_3)

    def get_color(self, y):
        b_c = (0.92, 0.84, 0.41)
        a_c = (0.1, 0.82, 0)
        per = y / c.MAX_HEIGHT
        x = ((a_c[0] - b_c[0]) * per) + b_c[0]
        y = ((b_c[1] - a_c[1]) * per) + a_c[1]
        z = ((b_c[2] - a_c[2]) * per) + a_c[2]
        return (x, y, z)
