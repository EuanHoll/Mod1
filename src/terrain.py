import map

def get_map_3d(map_data):
    verts = []
    edges = []
    y = x = 0
    while x < map_data.width:
        y = 0
        while y < map_data.height:
            i = (y * map_data.width) + x
            verts.append((x, int(map_data.array[i]), y))
            if (x + 1) % map_data.width != 0:
                edges.append((i, i + 1))
            if y > 0:
                edges.append((i, i - map_data.width))
            y += 1
        x += 1
    return map.Map_3d(verts, edges, map_data.width, map_data.height)
