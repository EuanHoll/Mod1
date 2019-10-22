

def apply_physics(voxel_data):
    stored = voxel_data.stored
    physics(voxel_data)
    if not (stored == voxel_data).all():
        voxel_data.redraw = True
    return voxel_data


def physics(voxel_data):
    z = 0
    while z < voxel_data.height:
        y = 0
        while y < voxel_data.depth:
            x = 0
            while x < voxel_data.width:
                val = voxel_data.stored[x][z][y]
                if z > 0 and val != -1:
                    val_1 = voxel_data.stored[x][z - 1][y]
                    if val_1 >= 0:
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
                            xy = should_move(x, y, z, voxel_data)
                            if x != xy[0] and y != xy[1]:
                                voxel_data.stored[xy[0]][z][xy[1]] += val
                                voxel_data.stored[x][z][y] = 0
                x += 1
            y += 1
        z += 1


def should_move(x, y, z, vd):
    smallest = vd.stored[x][z][y]
    xy = (x, y)
    if x - 1 >= 0:
        if smallest > vd.stored[x - 1][z][y]:
            smallest = vd.stored[x - 1][z][y]
            xy = (x - 1, y)
    if x + 1 < vd.width:
        if smallest > vd.stored[x + 1][z][y]:
            smallest = vd.stored[x + 1][z][y]
            xy = (x + 1, y)
    if y - 1 >= 0:
        if smallest > vd.stored[x][z][y - 1]:
            smallest = vd.stored[x][z][y - 1]
            xy = (x, y - 1)
    if y + 1 < vd.height:
        if smallest > vd.stored[x][z][y + 1]:
            smallest = vd.stored[x][z][y + 1]
            xy = (x, y + 1)
    if x + 1 < vd.width and y + 1 < vd.height:
        if smallest > vd.stored[x + 1][z][y + 1]:
            smallest = vd.stored[x + 1][z][y + 1]
            xy = (x + 1, y + 1)
    if x + 1 < vd.width and y - 1 >= 0:
        if smallest > vd.stored[x + 1][z][y - 1]:
            smallest = vd.stored[x + 1][z][y - 1]
            xy = (x + 1, y - 1)
    if x - 1 >= 0 and y + 1 < vd.height:
        if smallest > vd.stored[x - 1][z][y + 1]:
            smallest = vd.stored[x - 1][z][y + 1]
            xy = (x - 1, y + 1)
    if x - 1 >= 0 and y - 1 >= 0:
        if smallest > vd.stored[x - 1][z][y - 1]:
            smallest = vd.stored[x - 1][z][y - 1]
            xy = (x - 1, y - 1)
    return xy
