import numpy as np
import resource_functions as rf
from random import randint


def apply_physics(voxel_data, terrain, ws):
    if ws.const_wave == True:
        wall(voxel_data, terrain.voxel_data.stored)
    if ws.raining == True:
        rain(voxel_data, terrain.voxel_data.stored, ws)
    if ws.rising == True:
        rasing(voxel_data, terrain.voxel_data.stored, ws)
    stored = np.copy(voxel_data.stored)
    physics(voxel_data, terrain.voxel_data)
    if should_redraw(stored, voxel_data.stored, voxel_data.width, voxel_data.height, voxel_data.depth):
        voxel_data.redraw = True
    return voxel_data


def rasing(voxel_data, t_data, ws):
    if ws.last_rise == 0:
        ws.last_rise = rf.get_time()
    if rf.get_time() - ws.last_rise > 3:
        rise_to_layer(voxel_data, t_data, ws)
        ws.last_rise = 0
        if ws.layer + 1 < voxel_data.height - 2:
            ws.layer += 1
        voxel_data.redraw = True

def rise_to_layer(voxel_data, t_data, ws):
    z = 1
    while z < ws.layer:
        y = 1
        while y < voxel_data.depth - 1:
            x = 1
            while x < voxel_data.width - 1:
                if t_data[x][z][y] != 1:
                    voxel_data.stored[y][z][x] = 1
                x += 1
            y += 1
        z += 1

def rain(voxel_data, t_data, ws):
    vals = []
    if ws.last_rain == 0:
        ws.last_rain = rf.get_time()
    if rf.get_time() - ws.last_rain > 1:
        for i in range(0, randint(4, 30)):
            vals.append([randint(1, voxel_data.width - 2), voxel_data.height - randint(3, 8), randint(1, voxel_data.depth - 2), randint(1, 3)])
        apply_rain(voxel_data, t_data, vals)
        ws.last_rain = 0
        voxel_data.redraw = True


def apply_rain(voxel_data, t_data, rain):
    for val in rain:
        if t_data[val[0]][val[1]][val[2]] != 1:
            voxel_data.stored[val[0]][val[1]][val[2]] += val[3]


def wall(voxel_data, terrain):
    z = 1
    sze = int(voxel_data.depth / 2)
    while z < voxel_data.height - 1:
        y = 1
        while y < sze:
            x = 1
            while x < voxel_data.width - 1:
                if terrain[x][z][y] != 1:
                    voxel_data.stored[y][z][x] = 1
                x += 1
            y += 1
        z += 1
    voxel_data.redraw = True


def clear_under_terrain(voxel_data, t_data):
    z = 1
    while z < voxel_data.height:
        y = 0
        while y < voxel_data.depth:
            x = 0
            while x < voxel_data.width:
                if t_data[x][z][y] == 1:
                    voxel_data.stored[x][y][z] = 0
                x += 1
            y += 1
        z += 1


def should_redraw(pre, new, width, height, depth):
    z = 1
    while z < height - 1:
        y = 1
        while y < depth - 1:
            x = 1
            while x < width - 1:
                if pre[x][z][y] != new[x][z][y]:
                    return True
                x += 1
            y += 1
        z += 1
    return False


def physics(voxel_data, terrain):
    z = 1
    while z < voxel_data.height - 1:
        y = 1
        while y < voxel_data.depth - 1:
            x = 1
            while x < voxel_data.width - 1:
                val = voxel_data.stored[x][z][y]
                if z > 1 and val > 0:
                    val_1 = voxel_data.stored[x][z - 1][y]
                    if terrain.stored[x][z - 1][y] != 1 and val_1 >= 0:
                        if val_1 < 1:
                            i = 1 - val_1
                            if val > i:
                                val -= i
                                voxel_data.stored[x][z - 1][y] = 1
                            else:
                                voxel_data.stored[x][z - 1][y] = 1
                                voxel_data.stored[x][z][y] = 0
                                val = 0
                    if val > 0:
                        xy = should_move(x, y, z, voxel_data, terrain.stored)
                        if x != xy[0] and y != xy[1]:
                            voxel_data.stored[xy[0]][z][xy[1]] += val
                            voxel_data.stored[x][z][y] = 0
                x += 1
            y += 1
        z += 1


def should_move(x, y, z, vd, terrain):
    smallest = vd.stored[x][z][y]
    xy = (x, y)
    i = 0
    while i <= x + 1:
        j = 0
        while j <= y + 1:
            if vd.stored[i][z][j] < smallest:
                smallest = vd.stored[i][z][j]
                xy = (i, j)
            j += 1
        i += 1
    return xy
