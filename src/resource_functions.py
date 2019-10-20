import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
import time


def get_time():
    return int(round(time.time() * 1000))


def draw_text(text, position):
    font = pygame.font.Font(None, 64)
    textSurface = font.render(text, True, (255, 255, 255, 255), (0, 0, 0, 255))
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glRasterPos2d(*position)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)


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


def load_image(image_name):
    image_loc = "resources/images/" + image_name
    image = pygame.image.load(image_loc)
    if image is None:
        print("Image loading failed : " + image_name)
        return None
    return image
