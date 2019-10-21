from OpenGL.GL import *
from OpenGL.GLU import *
import const as c


class Map:
    """2D map class for initial storage of map"""
    def __init__(self, width, height, array):
        self.width = width
        self.height = height
        self.array = array


class Map_3d:
    """3D map class for 3d storage and rendering"""
    def __init__(self, verts, width, height):
        self.verts = verts
        self.width = width
        self.height = height

    def draw_map(self):
        """Draw the 3d map"""
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
                x += 1
            y += 1
        glEnd()

    def draw_trig(self, vert_1, vert_2, vert_3):
        """Draw an individual triangle"""
        glColor3fv(self.get_color(vert_1[2]))
        glVertex3fv(vert_1)
        glColor3fv(self.get_color(vert_2[2]))
        glVertex3fv(vert_2)
        glColor3fv(self.get_color(vert_3[2]))
        glVertex3fv(vert_3)

    def get_color(self, y):
        """Get the colour to draw the vertex"""
        b_c = (0.92, 0.84, 0.41)
        a_c = (0.1, 0.82, 0)
        per = y / c.MAX_HEIGHT
        x = ((a_c[0] - b_c[0]) * per) + b_c[0]
        y = ((b_c[1] - a_c[1]) * per) + a_c[1]
        z = ((b_c[2] - a_c[2]) * per) + a_c[2]
        return x, y, z

    def draw_lines(self, vert_1, vert_2, vert_3, vert_4):
        """Draw a single quad (in GL_LINES format)"""
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
