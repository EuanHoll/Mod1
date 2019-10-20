import pygame
from OpenGL.GL import *


# Loads an image to the correct icon format
def load_icon(icon_name):
    image_loc = "resources/images/" + icon_name
    image = pygame.image.load(image_loc)
    if image is None:
        print("Icon loading failed : " + icon_name)
        return None
    surface = pygame.Surface((32, 32))
    key = (0, 255, 0)
    surface.fill(key)
    surface.set_colorkey(key)
    surface.blit(image, (0, 0))
    return surface


# Loads an image to a surface
def load_image(image_name):
    image_loc = "resources/images/" + image_name
    image = pygame.image.load(image_loc)
    if image is None:
        print("Image loading failed : " + image_name)
        return None
    return image


# Loads shader from file
def load_shader(file_loc, shader_type):
    if not file_loc.endswith('.glsl'):
        print("Please choose a .glsl file")
        return None
    try:
         with open(file_loc, "r") as glsl_file:
            data = glsl_file.read()
    except:
        print("Please chose a valid .glsl file")
        pygame.quit()
        quit()
    shader_id = glCreateShader(shader_type)
    glShaderSource(shader_id, data)
    glCompileShader(shader_id)
    if glGetShaderiv(shader_id, GL_COMPILE_STATUS) == GL_FALSE:
        print(glGetShaderInfoLog(shader_id, 500))
        print("Could not compile shader : " + file_loc)
        pygame.quit()
        quit()
    return shader_id
