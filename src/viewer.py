import voxel as vx
import terrain
import resource_functions as rf
import pygame
import const as c
import water_physics as wp
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


raining = False
constant_wave = False
rising = False


def viewer(map_data):
    """The window display initialization"""
    pygame.init()
    screen = pygame.display.set_mode((c.S_WIDTH, c.S_HEIGHT), DOUBLEBUF|OPENGL|RESIZABLE)
    pygame.display.set_caption("Mod1")
    pygame.display.set_icon(rf.load_icon("icon.png"))
    gluPerspective(60, c.S_RATIO, 0.1, 1000)
    glTranslate(-10, -4, -40)
    glRotatef(30, 1, 0, 0)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glClearColor(0.411, 0.451, 0.5412, 1)
    loop(screen, map_data)


def loop(screen, map_data):
    """The main game loop"""
    running = True
    ter = terrain.get_terrain(map_data)
    water = vx.Voxel(vx.Voxel_Data(22, c.MAX_HEIGHT + 2, 22, 0.3, 2), "water.ver", "water.frag")
    wp.clear_under_terrain(water.voxel_data, ter.voxel_data.stored)
    ws = c.WaterSim()
    start_time = rf.get_time()
    counter = 0
    while running:
        for event in pygame.event.get():
            running = event_handling(event, water, ter, ws)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        handle_water(water, ter, ws)
        water.draw_mesh_shader()
        ter.draw_mesh_shader()
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


def handle_water(voxel, ter, ws):
    voxel.voxel_data = wp.apply_physics(voxel.voxel_data, ter, ws)


def event_handling(event, water, ter, ws):
    """Pygame event handling"""
    if event.type == pygame.QUIT:
        return False
    if event.type == pygame.KEYDOWN:
        return key_controls(event, water, ter, ws)
    return True


def key_controls(event, water, ter, ws):
    """Key event handling"""
    if event.key == pygame.K_ESCAPE:
        return False
    if event.key == pygame.K_1:
        wp.wall(water.voxel_data, ter.voxel_data.stored)
        wp.clear_under_terrain(water.voxel_data, ter.voxel_data.stored)
    if event.key == pygame.K_0:
        water.voxel_data.stored = water.voxel_data.create_empty()
        water.voxel_data.redraw = True
    if event.key == pygame.K_9:
        water.voxel_data.stored = water.voxel_data.create_full()
        wp.clear_under_terrain(water.voxel_data, ter.voxel_data.stored)
        water.voxel_data.redraw = True
    if event.key == pygame.K_8:
        water.voxel_data.stored = water.voxel_data.create_level()
        wp.clear_under_terrain(water.voxel_data, ter.voxel_data.stored)
        water.voxel_data.redraw = True
    if event.key == pygame.K_7:
        water.voxel_data.stored = water.voxel_data.create_random()
        wp.clear_under_terrain(water.voxel_data, ter.voxel_data.stored)
        water.voxel_data.redraw = True
    if event.key == pygame.K_2:
        ws.const_wave = not ws.const_wave
    if event.key == pygame.K_3:
        ws.rising = not ws.rising
    if event.key == pygame.K_4:
        ws.raining = not ws.raining


    return True
