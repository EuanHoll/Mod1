

# Initial map reading object
class Map:
    def __init__(self, width, height, array):
        self.width = width
        self.height = height
        self.array = array


# 3D map information object which will get converted into a voa
class Info_3d:
    def __init__(self, verts, indices):
        self.verts = verts
        self.indices = indices
