'''
Reads a DOOM engine WAD and returns a lump directory and list of all lumps
'''

import struct
from map import Map

wad_name = 'doom2.wad'
wadfile = open(wad_name, 'rb')
dump = open('dump.txt', 'a')
directory = open('directory.txt', 'a')


class Wad:
    def __init__(self, wad_file):
        self.wad_file = wad_file
        self.wad_header = struct.unpack('4sll', self.wad_file.read(12))
        self.wad_type = self.wad_header[0].decode('utf-8')
        self.num_lumps = self.wad_header[1]
        self.directory_location = self.wad_header[2]
        self.lump_list = []

        self.wad_palette_list = []
        self.wad_colormap_list = []
        self.wad_endoom_list = []
        self.wad_demo_list = []
        self.wad_genmidi_list = []
        self.wad_gus_list = []
        self.wad_soundeffect_list = []
        self.wad_texture_index_list = []
        self.wad_map_list = []

    def index(self):
        self.wad_file.seek(self.directory_location)

        for i in range(0, self.num_lumps):
            lump_index = struct.unpack('ll8s', self.wad_file.read(16))  # lump data is read
            lump_start = lump_index[0]
            lump_size = lump_index[1]
            lump_name = lump_index[2]
            lump_name = lump_name.decode('UTF-8').strip('\x00')

            index_offset = self.wad_file.tell()         # store current wad offset. Will set pointer back to this once
            print('current wad offset {}'.format(index_offset))
            self.wad_file.seek(lump_start)

            print('Lump offset {}'.format(lump_start))
            lump_data = self.wad_file.read(lump_size)
            self.lump_list.append(Lump(i, lump_start, lump_size, lump_name, lump_data))
            self.wad_file.seek(index_offset)
            print('Return to wad offset {}'.format(index_offset))

    def format_lumps(self):
        for lump in self.lump_list:
            if lump.lump_name.startswith('MAP'):
                map_label = lump.lump_id
                map_cluster =[lump, self.lump_list[map_label+1], self.lump_list[map_label+2],
                              self.lump_list[map_label+3], self.lump_list[map_label+4], self.lump_list[map_label+5],
                              self.lump_list[map_label+6], self.lump_list[map_label+7], self.lump_list[map_label+8],
                              self.lump_list[map_label+9], self.lump_list[map_label+10]]
                self.wad_map_list.append(Map(map_cluster))


class Lump:
    def __init__(self, lump_id, offset, size, lump_name, lump_data):
        self.lump_id = lump_id
        self.offset = offset
        self.size = size
        self.lump_name = lump_name
        self.lump_data = lump_data

