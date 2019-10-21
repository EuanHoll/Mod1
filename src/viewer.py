import voxel as vx
import terrain
import resource_functions as rf
import pygame
import const as c
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def viewer(map_data):
    """The window display initialization"""
    pygame.init()
    screen = pygame.display.set_mode((c.S_WIDTH, c.S_HEIGHT), DOUBLEBUF|OPENGL|RESIZABLE)
    pygame.display.set_caption("Mod1")
    pygame.display.set_icon(rf.load_icon("icon.png"))
    gluPerspective(60, c.S_RATIO, 0.1, 1000)
    map_3d = terrain.get_map_3d(map_data)
    glTranslate(-(map_3d.width / 2), -(map_3d.height / 2), -10)
    glRotatef(45, -90, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.411, 0.451, 0.5412, 1)
    loop(screen, map_3d)


def loop(screen, map_3d):
    """The main game loop"""
    running = True
    water = vx.Voxel(vx.Voxel_Data(map_3d.width * 10, 10, map_3d.height * 10, 0.6, 2), map_3d.width, 10, map_3d.height)
    start_time = rf.get_time()
    fps = 0
    counter = 0
    while running:
        for event in pygame.event.get():
            running = event_handling(event)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        map_3d.draw_map()
        water.draw_mesh()
        time = rf.get_time() - start_time
        if time > 1:
            fps = counter / time
            pygame.display.set_caption("Mod1 : FPS (" + str(int(fps)) + ")")
            counter = 0
            start_time = rf.get_time()
        pygame.display.flip()
        counter += 1
    pygame.quit()
    quit()


def event_handling(event):
    """Pygame event handling"""
    if event.type == pygame.QUIT:
        return False
    if event.type == pygame.KEYDOWN:
        return key_controls(event)
    return True


def key_controls(event):
    """Key event handling"""
    if event.key == pygame.K_ESCAPE:
        return False
    return True
