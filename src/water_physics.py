import numpy as np


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


def apply_physics(voxel_data, terrain):
    stored = np.copy(voxel_data.stored)
    physics(voxel_data, terrain.voxel_data)
    #if should_redraw(stored, voxel_data.stored, voxel_data.width, voxel_data.height, voxel_data.depth):
    voxel_data.redraw = True
        #print("Here")
    return voxel_data


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
                if z > 1 and val != -1:
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
    if x - 1 >= 0 and terrain[x -1][z][y] != 1:
        if smallest > vd.stored[x - 1][z][y]:
            smallest = vd.stored[x - 1][z][y]
            xy = (x - 1, y)
    if x + 1 < vd.width and terrain[x + 1][z][y] != 1:
        if smallest > vd.stored[x + 1][z][y]:
            smallest = vd.stored[x + 1][z][y]
            xy = (x + 1, y)
    if y - 1 >= 0 and terrain[x][z][y - 1] != 1:
        if smallest > vd.stored[x][z][y - 1]:
            smallest = vd.stored[x][z][y - 1]
            xy = (x, y - 1)
    if y + 1 < vd.height and terrain[x][z][y + 1] != 1:
        if smallest > vd.stored[x][z][y + 1]:
            smallest = vd.stored[x][z][y + 1]
            xy = (x, y + 1)
    if x + 1 < vd.width and y + 1 < vd.height and terrain[x + 1][z][y + 1] != 1:
        if smallest > vd.stored[x + 1][z][y + 1]:
            smallest = vd.stored[x + 1][z][y + 1]
            xy = (x + 1, y + 1)
    if x + 1 < vd.width and y - 1 >= 0 and terrain[x + 1][z][y - 1] != 1:
        if smallest > vd.stored[x + 1][z][y - 1]:
            smallest = vd.stored[x + 1][z][y - 1]
            xy = (x + 1, y - 1)
    if x - 1 >= 0 and y + 1 < vd.height and terrain[x - 1][z][y + 1] != 1:
        if smallest > vd.stored[x - 1][z][y + 1]:
            smallest = vd.stored[x - 1][z][y + 1]
            xy = (x - 1, y + 1)
    if x - 1 >= 0 and y - 1 >= 0 and terrain[x - 1][z][y - 1] != 1:
        if smallest > vd.stored[x - 1][z][y - 1]:
            smallest = vd.stored[x - 1][z][y - 1]
            xy = (x - 1, y - 1)
    return xy
