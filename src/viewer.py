import map
import terrain
import resource_functions as rf
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def viewer(map_data):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Mod1")
    pygame.display.set_icon(rf.load_icon("icon.png"))
    gluPerspective(60, (1280/720), 0.1, 1000)
    glTranslatef(-4, -4, -10)
    glRotatef(45, -90, 0, 0)
    glEnable(GL_DEPTH_TEST)
    loop(screen, map_data)


def loop(screen, map_data):
    running = True
    map_3d = terrain.get_map_3d(map_data)
    while running:
        for event in pygame.event.get():
            running = event_handling(event)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        map_3d.draw_map()
        pygame.display.flip()
    pygame.quit()
    quit()


def event_handling(event):
    if event.type == pygame.QUIT:
        return False
    if event.type == pygame.KEYDOWN:
        return key_controls(event)
    return True


def key_controls(event):
    if event.key == pygame.K_ESCAPE:
        return False
    return True
