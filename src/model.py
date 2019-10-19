from OpenGL.GL import *
import numpy as np

class Model:
    def __init__(self, vao_id, vbos, vert_count):
        self.vao_id = vao_id
        self.vbo_ids = vbos
        self.vert_count = vert_count


def clean_up_model(model):
    vaos = [model.vao_id]
    glDeleteVertexArrays(1, vaos)
    glDeleteBuffers(len(model.vbo_ids), np.asarray(model.vbo_ids))


def create_model_from_3d(info_3d):
    vao_id = create_vao()
    vbos = create_data(info_3d)
    unbind_vao()
    return Model(vao_id, vbos, len(info_3d.verts))


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


def create_vao():
    vao_id = glGenVertexArrays(1)
    glBindVertexArray(vao_id)
    return vao_id


def unbind_vao():
    glBindVertexArray(0)
