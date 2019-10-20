import map

def get_map_3d(map_data):
    verts = []
    edges = []
    y = 0
    while y < map_data.height:
        x = 0
        while x < map_data.width:
            i = (y * map_data.width) + x
            verts.append((x, y, int(map_data.array[i])))
            if (x + 1) % map_data.width != 0:
                edges.append((i, i + 1))
            if y > 0:
                edges.append((i, i - map_data.width))
            x += 1
        y += 1
    return map.Map_3d(verts, edges, map_data.width, map_data.height)
