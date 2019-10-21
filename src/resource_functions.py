import pygame
import time


def get_time():
    """Wrapper for time"""
    return time.time()


def load_icon(icon_name):
    """Load game icon"""
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
    """Load image to surface"""
    image_loc = "resources/images/" + image_name
    image = pygame.image.load(image_loc)
    if image is None:
        print("Image loading failed : " + image_name)
        return None
    return image



def read_shader(filename):
    """Load text from shader file"""
    return open("resources/shaders/" + filename, 'r').read()
