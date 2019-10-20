import resource_functions as rf
from OpenGL.GL import *


# Shader program object
class Shader:

    def __init__(self, vert_sha_file, frag_sha_file):
        self.vert_sha_id = rf.load_shader(vert_sha_file, GL_VERTEX_SHADER)
        self.frag_sha_id = rf.load_shader(frag_sha_file, GL_FRAGMENT_SHADER)
        self.prog_id = glCreateProgram()
        glAttachShader(self.prog_id, self.vert_sha_id)
        glAttachShader(self.prog_id, self.frag_sha_id)
        self.bind_attributes()
        glLinkProgram(self.prog_id)
        glValidateProgram(self.prog_id)
        self.trans_matrix = self.get_uniform_location("transformMatrix")
        self.project_matrix = self.get_uniform_location("projectMatrix")

    # Load transform matrix
    def load_transform_matrix(self, trans_matrix):
        self.load_matrix(self.trans_matrix, trans_matrix)

    # Load projection matrix
    def load_project_matrix(self, project_matrix):
        self.load_matrix(self.project_matrix, project_matrix)

    # Gets uniform location
    def get_uniform_location(self, uniform_name):
        return glGetUniformLocation(self.prog_id, uniform_name)

    # Loads float to uniform
    def load_float(self, uniform_loc, val):
        glUniform1f(uniform_loc, val)

    # Loads vec3 to uniform
    def load_vec3(self, uniform_loc, val):
        glUniform3f(uniform_loc, val)

    # Load bool
    def load_bool(self, uniform_loc, val):
        uni_val = 0
        if val:
            uni_val = 1
        glUniform1f(uniform_loc, uni_val)

    # Load Matrix
    def load_matrix(self, uniform_loc, matrix):
        glUniformMatrix4fv(uniform_loc, 1, GL_FALSE, matrix)

    # Starts shader program
    def start_shader(self):
        glUseProgram(self.prog_id)

    # Stops shader program
    def stop_shader(self):
        glUseProgram(0)

    # Cleans up shader
    def clean_up(self):
        self.stop_shader()
        glDetachShader(self.prog_id, self.vert_sha_id)
        glDetachShader(self.prog_id, self.frag_sha_id)
        glDeleteShader(self.vert_sha_id)
        glDeleteShader(self.frag_sha_id)
        glDeleteProgram(self.prog_id)

    # Binds All Attributes
    def bind_attributes(self):
        self.bind_attribute(0, "position")

    # Binds Attribute
    def bind_attribute(self, attribute, var_name):
        glBindAttribLocation(self.prog_id, attribute, var_name)
