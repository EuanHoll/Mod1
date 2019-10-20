import voxel as vx
import terrain
import resource_functions as rf
import pygame
import const as c
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def viewer(map_data):
    pygame.init()
    screen = pygame.display.set_mode((c.S_WIDTH, c.S_HEIGHT), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Mod1")
    pygame.display.set_icon(rf.load_icon("icon.png"))
    gluPerspective(60, c.S_RATIO, 0.1, 1000)
    map_3d = terrain.get_map_3d(map_data)
    glRotatef(45, -90, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.411, 0.451, 0.5412, 1)
    loop(screen, map_3d)


def loop(screen, map_3d):
    running = True
    water = vx.Voxel(vx.Voxel_Data(10, 10, 10, 0.6, 2))
    glTranslatef(-(water.voxel_data.width / 2), -(water.voxel_data.depth / 2), -10)
    while running:
        for event in pygame.event.get():
            running = event_handling(event)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        map_3d.draw_map()
        water.draw_mesh()
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
