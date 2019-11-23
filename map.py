import struct

# map_cluster = {'name': lump,
#                'things': self.lump_list[map_label + 1],
#                'linedefs': self.lump_list[map_label + 2],
#                'sidedefs': self.lump_list[map_label + 3],
#                'vertexes': self.lump_list[map_label + 4],
#                'segs': self.lump_list[map_label + 5],
#                'ssectors': self.lump_list[map_label + 6],
#                'nodes': self.lump_list[map_label + 7],
#                'sectors': self.lump_list[map_label + 8],
#                'reject': self.lump_list[map_label + 9],
#                'blockmap': self.lump_list[map_label + 10]}
# self.wad_map_list.append(Map(map_cluster))

lump_types = ['label', 'things', 'linedefs', 'sidedefs', 'vertexes',
              'segs', 'ssectors', 'nodes', 'sectors', 'reject', 'blockmap']


class Map:
    def __init__(self, cluster):
        self.cluster = cluster
        self.map_lumps = []

    def unpack(self):           # unpacks cluster of lumps into lists containing things, linedefs, segs, etc.
        x=0
        for lump in self.cluster:
            self.map_lumps.append(Container(lump, lump_types[x]))
            # print(x)
            x += 1


class Container:
    def __init__(self, lump, lump_type):
        self.lump_data = lump
        self.type = lump_type
        self.entries = []

    def unpack(self):
        pass


class Thing:
    def __init__(self, things):             # struct 'hhhhh' 10 bytes
        self.lump = things


class Linedef:                             # struct 'hhhhhhh' 14 bytes
    def __init__(self, linedefs):
        self.lump = linedefs


class Sidedef:                             # struct 'hh sss h' 30 bytes
    def __init__(self, sidedefs):
        self.lump = sidedefs


class Vertex:                             # struct
    def __init__(self, vertexes):
        self.lump = vertexes


class Seg:                                 # struct
    def __init__(self, segs):
        self.lump = segs


class SSector:                             # struct
    def __init__(self, ssectors):
        self.ssectors_lump = ssectors


class Node:                                # struct
    def __init__(self, nodes):
        self.nodes_lump = nodes


class Sector:                              # struct
    def __init__(self, sectors):
        self.sectors_lump = sectors


class Rejec:                               # struct
    def __init__(self, reject):
        self.reject_lump = reject


class Blockmap:                             # struct
    def __init__(self, blockmap):
        self.blockmap_lump = blockmap


