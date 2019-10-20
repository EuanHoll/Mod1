from OpenGL.GL import *
import util_functions as uf


# Prepares frame to be rendered to
def prepare_frame():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)


# Renders passed model to frame
def render_model(model, shader):
    glBindVertexArray(model.vao_id)
    glEnableVertexAttribArray(0)
    mat = uf.create_trans_matrix([0, 0, 0], [0, 0, 0], 1)
    shader.load_transform_matrix(mat)
    glDrawElements(GL_LINES, model.vert_count, GL_UNSIGNED_INT, None)
    glDisableVertexAttribArray(0)
    glBindVertexArray(0)
