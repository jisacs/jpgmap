import networkx as nx
from .pixel import Pixel


class Graph():
    def __init__(self, _map):
        self.gnx = nx.Graph()

        for pixel in _map.get_pixels_road_ordered():
            self.gnx.add_node(pixel.pos())

        for pixel in _map.get_pixels_road_ordered():
                neighbourgs = _map.get_neighbours_road(pixel)
                for neighbourg in  neighbourgs:
                    self.gnx.add_edge(pixel.pos(), neighbourg.pos())
                    #print("Add edge {} {}".format(pixel.pos(), neighbourg.pos()))

        start = _map.get_pixels_ordered()[0]
        end =_map.get_pixels_ordered()[-1]
        print("Start Stop edge {} {}".format(start.pos(), end.pos()))
        for  path  in nx.all_simple_paths(self.gnx, (2,2), (7,7)):
            print("PATH {}".format(path))




