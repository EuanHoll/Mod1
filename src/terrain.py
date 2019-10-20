import map


def get_map_3d(map_data):
    verts = []
    y = 0
    while y < map_data.height + 2:
        x = 0
        while x < map_data.width + 2:
            if 0 <= x - 1 < map_data.width and 0 <= y - 1 < map_data.height:
                i = ((y - 1) * map_data.width) + x - 1
                verts.append((x, y, int(map_data.array[i])))
            else:
                verts.append((x, y, 0))
            x += 1
        y += 1
    print_verts(verts, map_data.width + 2, map_data.height + 2)
    return map.Map_3d(verts, map_data.width + 2, map_data.height + 2)


def print_verts(verts, width, height):
    i = 0
    while i < height:
        print(verts[i * width:(i + 1) * width])
        i += 1
