import terrain
import resource_functions as rf
import pygame
import model
import renderer
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def viewer(map_data):
    pygame.init()
    screen = pygame.display.set_mode((1280, 720), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Mod1")
    pygame.display.set_icon(rf.load_icon("icon.png"))
    gluPerspective(60, (1280/720), 0.1, 1000)
    glTranslatef(0, 2, -5)
    loop(map_data)


def loop(map_data):
    running = True
    model_terrain = model.create_model_from_3d(terrain.get_map_verts(map_data))
    while running:
        for event in pygame.event.get():
            running = event_handling(event)
        print("Before Prep")
        renderer.prepare_frame()
        print("Render Model")
        renderer.render_model(model_terrain)
        print("Flip")
        pygame.display.flip()
    model.clean_up_model(model_terrain)
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
    if event.key == pygame.K_w:
        glTranslatef(0, 0, 1)
    if event.key == pygame.K_s:
        glTranslatef(0, 0, -1)
    if event.key == pygame.K_a:
        glTranslatef(1, 0, 0)
    if event.key == pygame.K_d:
        glTranslatef(-1, 0, 0)
    if event.key == pygame.K_z:
        glTranslatef(0, 1, 0)
    if event.key == pygame.K_x:
        glTranslatef(0, -1, 0)
    return True
