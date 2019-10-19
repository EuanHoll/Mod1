from OpenGL.GL import *
import numpy as np

# Opengl VAO and VBO information
class Model:
    def __init__(self, vao_id, vbos, vert_count):
        self.vao_id = vao_id
        self.vbo_ids = vbos
        self.vert_count = vert_count


# Deletes VAO and VBO information from buffers
def clean_up_model(model):
    vaos = [model.vao_id]
    glDeleteVertexArrays(1, vaos)
    glDeleteBuffers(len(model.vbo_ids), np.asarray(model.vbo_ids))


# Creates VAO and VBO information from Info_3d information
def create_model_from_3d(info_3d):
    vao_id = create_vao()
    vbos = create_data(info_3d)
    unbind_vao()
    return Model(vao_id, vbos, len(info_3d.verts))


# Converts verts and indices to VBO information
def create_data(info_3d):
    vbos = [glGenBuffers(1), glGenBuffers(1)]
    glBindBuffer(GL_ARRAY_BUFFER, vbos[0])
    glBufferData(GL_ARRAY_BUFFER, 4 * len(info_3d.verts), np.asarray(info_3d.verts), GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vbos[1])
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 4 * len(info_3d.indices), np.asarray(info_3d.indices), GL_STATIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    return vbos


# Creates the initial VAO
def create_vao():
    vao_id = glGenVertexArrays(1)
    glBindVertexArray(vao_id)
    return vao_id


# Unbinds the VAO from the buffer
def unbind_vao():
    glBindVertexArray(0)
