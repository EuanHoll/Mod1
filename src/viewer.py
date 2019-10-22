import voxel as vx
import terrain
import resource_functions as rf
import pygame
import const as c
import water_physics as wp
import numpy as np
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
    ter = terrain.get_terrain(map_data)
    glTranslate(-(ter.voxel_data.width / 2), -ter.voxel_data.height, -ter.voxel_data.depth)
    glRotatef(45, -90, 0, 0)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glClearColor(0.411, 0.451, 0.5412, 1)
    loop(screen, ter)


def loop(screen, ter):
    """The main game loop"""
    running = True
    water = vx.Voxel(vx.Voxel_Data(ter.voxel_data.width, c.MAX_HEIGHT, ter.voxel_data.depth, 0.6, 0), "water.ver", "water.frag")
    start_time = rf.get_time()
    fps = 0
    counter = 0
    while running:
        for event in pygame.event.get():
            running = event_handling(event, water, ter)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        ter.draw_mesh_shader()
        #handle_water(water, ter)
        water.draw_mesh_shader()
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


def handle_water(voxel, ter):
    voxel.voxel_data = wp.apply_physics(voxel.voxel_data, ter)


def event_handling(event, water, ter):
    """Pygame event handling"""
    if event.type == pygame.QUIT:
        return False
    if event.type == pygame.KEYDOWN:
        return key_controls(event, water, ter)
    return True


def key_controls(event, water, ter):
    """Key event handling"""
    if event.key == pygame.K_ESCAPE:
        return False
    if event.key == pygame.K_1:
        wp.wall(water.voxel_data, ter.voxel_data.stored)
    if event.key == pygame.K_0:
        water.voxel_data.stored = water.voxel_data.create_empty()
        water.voxel_data.redraw = True
    if event.key == pygame.K_9:
        water.voxel_data.stored = water.voxel_data.create_full()
        water.voxel_data.redraw = True
    if event.key == pygame.K_8:
        water.voxel_data.stored = water.voxel_data.create_level()
        water.voxel_data.redraw = True
    if event.key == pygame.K_7:
        water.voxel_data.stored = water.voxel_data.create_random()
        water.voxel_data.redraw = True
    return True
