import numpy as np
import math


# Creates a transformation matrix
def create_trans_matrix(pos, rot, scale):
    mat = np.empty((4, 4))
    translate_matrix(mat, pos)
    rotate_matrix(mat, rot)
    scale_matrix(mat, scale)
    return mat


# Translate matrix
def translate_matrix(matrix, vec3):
    matrix[3, :] += matrix[0, :] * vec3[0] + matrix[1, :] * vec3[1] + matrix[2, :] * vec3[2]

# Rotate matrix
def rotate_matrix(matrix, rot):
    rx, ry, rz = math.radians(rot[0]), math.radians(rot[1]), math.radians(rot[2])
    m_sincos = [[math.sin(rx), math.cos(rx)],
                [math.sin(ry), math.cos(ry)],
                [math.sin(rz), math.cos(rz)]]
    matrix[0, 0] = m_sincos[1][1] * m_sincos[2][1]
    matrix[0, 1] = (m_sincos[1][1] * m_sincos[2][0] * m_sincos[0][0]) - (m_sincos[1][0] * m_sincos[0][1])
    matrix[0, 2] = (m_sincos[1][1] * m_sincos[2][0] * m_sincos[0][1]) + (m_sincos[1][0] * m_sincos[0][0])
    matrix[1, 0] = m_sincos[1][0] * m_sincos[2][1]
    matrix[1, 1] = (m_sincos[1][0] * m_sincos[2][0] * m_sincos[0][0]) - (m_sincos[1][1] * m_sincos[0][1])
    matrix[1, 2] = (m_sincos[1][0] * m_sincos[2][0] * m_sincos[0][1]) + (m_sincos[1][1] * m_sincos[0][0])
    matrix[2, 0] = -m_sincos[2][0]
    matrix[2, 1] = m_sincos[2][1] * m_sincos[0][0]
    matrix[2, 2] = m_sincos[2][1] * m_sincos[0][1]

# Scale matrix
def scale_matrix(matrix, scale):
    matrix[0:3, :] *= scale
