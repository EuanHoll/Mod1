import map
import const as c
import voxel as vx
import numpy as np


def get_terrain(map_data):
    vd = get_voxel_data(map_data)
    v = vx.Voxel(vd, "terrain.ver", "terrain.frag")
    return v



def get_voxel_data(map_data):
    map3d = get_map_3d(map_data)
    vd = vx.Voxel_Data(int(map3d.width + 2), int(c.MAX_HEIGHT + 2), int(map3d.height + 2), 0.4, 0)
    vd.stored = get_voxel_map(map3d, vd)
    return vd


def get_voxel_map(map_data, vd):
    stored = np.empty((vd.width, vd.height, vd.depth))
    stored.fill(0)
    z = 1
    while z < vd.height - 1:
        y = 1
        while y < vd.depth - 1:
            x = 1
            while x < vd.width - 1:
                if z < map_data.verts[((y - 1) * (vd.width - 2)) + x - 1][2] * 10:
                    stored[x][z][y] = 1
                x += 1
            y += 1
        z += 1
    return stored


def get_map_3d(map_data):
    """Converts the raw terrain map into a verts"""
    verts = []
    y = 0
    while y < map_data.height + 2:
        x = 0
        while x < map_data.width + 2:
            if 0 <= x - 1 < map_data.width and 0 <= y - 1 < map_data.height:
                i = ((y - 1) * map_data.width) + x - 1
                if int(map_data.array[i]) > c.MAX_HEIGHT - 1:
                    print("The max height of the terrain is " + str(c.MAX_HEIGHT - 1))
                    quit()
                verts.append([x, y, int(map_data.array[i])])
            else:
                verts.append([x, y, 0])
            x += 1
        y += 1
    verts = expand_map(verts, (map_data.width + 2, map_data.height + 2), (20, 20))
    smooth_verts(verts, 20, 20)
    return map.Map3d(verts, 20,20)


def expand_map(verts, now, expanded):
    ver = []
    y = 0
    while y < expanded[1]:
        x = 0
        while x < expanded[0]:
            z = get_from_map((int((x / expanded[0]) * now[0]), int((y / expanded[1]) * now[1])), 1, now[0], verts)
            ver.append(([x, y, z]))
            x += 1
        y += 1
    return ver


def get_from_map(pos, percent, width, verts):
    if pos[0] + 1 < width:
        z_0 = verts[(pos[1] * width) + pos[0]][2]
        z_1 = verts[(pos[1] * width) + pos[0] + 1][2]
        return z_0
    return verts[(pos[1] * width) + pos[0]][2]


def smooth_verts(verts, width, height):
    smooth_1(verts, width, height)
    smooth_0(verts, width, height)
    smooth_2(verts, width, height)
    smooth_3(verts, width, height)


def smooth_0(verts, width, height):
    i = 0
    length = width * height
    while i < length:
        if i % width == 0 and int(i / width) > 0:
            verts[i][2] = (verts[i][2] + verts[i - width][2]) / 2
        elif i % width > 0 and int(i / width) == 0:
            verts[i][2] = (verts[i][2] + verts[i - 1][2]) / 2
        elif i % width > 0 and int(i / width) > 0:
            verts[i][2] = (verts[i][2] + verts[i - width][2] + verts[i - 1][2]) / 3
        i += 1


def smooth_1(verts, width, height):
    i = 0
    length = width * height
    while i < length:
        if i % width == 0 and int(i / width) + 1 < height:
            verts[i][2] = (verts[i][2] + verts[i + width][2]) / 2
        elif (i + 1) % width > 0 and int(i / width) == 0:
            verts[i][2] = (verts[i][2] + verts[i + 1][2]) / 2
        elif (i + 1) % width > 0 and int(i / width) + 1 < height:
            verts[i][2] = (verts[i][2] + verts[i + width][2] + verts[i + 1][2]) / 3
        i += 1


def smooth_2(verts, width, height):
    i = 0
    length = width * height
    while i < length:
        if i % width == 0 and int(i / width) > 0:
            verts[i][2] = (verts[i][2] + verts[i - width][2]) / 2
        elif (i + 1) % width > 0 and int(i / width) == 0:
            verts[i][2] = (verts[i][2] + verts[i + 1][2]) / 2
        elif (i + 1) % width > 0 and int(i / width) > 0:
            verts[i][2] = (verts[i][2] + verts[i - width][2] + verts[i + 1][2]) / 3
        i += 1


def smooth_3(verts, width, height):
    i = 0
    length = width * height
    while i < length:
        if i % width == 0 and int(i / width) + 1 < height:
            verts[i][2] = (verts[i][2] + verts[i + width][2]) / 2
        elif i % width > 0 and int(i / width) == 0:
            verts[i][2] = (verts[i][2] + verts[i - 1][2]) / 2
        elif i % width > 0 and int(i / width) + 1 < height:
            verts[i][2] = (verts[i][2] + verts[i + width][2] + verts[i - 1][2]) / 3
        i += 1


def print_verts(verts, width, height):
    """Prints the raw terrain map"""
    i = 0
    while i < height:
        print(verts[i * width:(i + 1) * width])
        i += 1
