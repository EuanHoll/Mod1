from OpenGL.GL import *


# Prepares frame to be rendered to
def prepare_frame():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)


# Renders passed model to frame
def render_model(model):
    glBindVertexArray(model.vao_id)
    glEnableVertexAttribArray(0)
    glDrawElements(GL_TRIANGLES, model.vert_count, GL_UNSIGNED_INT, None)
    glDisableVertexAttribArray(0)
    glBindVertexArray(0)
