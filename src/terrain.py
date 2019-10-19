import map


def get_map_verts(map_data):
    verts = []
    indices = []
    x = 0
    while x < map_data.width:
        y = 0
        while y < map_data.height:
            i = (y * map_data.width) + x
            verts.append(float(x))
            verts.append(float(map_data.array[i]))
            verts.append(float(y))
            if (x + 1) % map_data.width != 0 and y > 0:
                append_indices(indices, i, map_data)

            y += 1
        x += 1
    return map.Info_3d(verts, indices)


def append_indices(indices, i, map_data):
    indices.append(i - map_data.width)
    indices.append(i - map_data.width + 1)
    indices.append(i)
    indices.append(i)
    indices.append(i + 1)
    indices.append(i + 1 - map_data.width)