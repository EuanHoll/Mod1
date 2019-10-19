from OpenGL.GL import *
from OpenGL.GLU import *


def prepare_frame():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)


def render_model(model):
    glBindVertexArray(model.vao_id)
    glEnableVertexAttribArray(0)
    glDrawElements(GL_TRIANGLES, model.vert_count, GL_UNSIGNED_INT, None)
    glDisableVertexAttribArray(0)
    glBindVertexArray(0)
