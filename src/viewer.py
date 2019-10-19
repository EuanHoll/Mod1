import map
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def viewer(map_data):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Mod1")
    gluPerspective(60, (1280/720), 0.1, 1000)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(0, 0, 0, 0)
    loop(screen)

def loop(screen):
    running = True
    while running:
        for event in pygame.event.get():
            running = event_handling(event)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        pygame.display.flip()

def event_handling(event):
    if event.type == pygame.QUIT:
        return False
    return True