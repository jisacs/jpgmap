import networkx as nx
from .pixel import Pixel
import networkx

class Graph():
    def __init__(self, _map):
        self.gnx = nx.Graph()

        for pixel in _map.get_pixels_road_ordered():
            if len(pixel.neighbours) < 7:
                self.gnx.add_node(pixel.pos())


        for pixel in _map.get_pixels_road_ordered():
            neighbourgs = _map.get_neighbours_road(pixel)
            for neighbourg in  neighbourgs:
                self.gnx.add_edge(pixel.pos(), neighbourg.pos())


    def get_paths(self, pixels):
        start = pixels[0]
        end = pixels[1]
        try:
            return  nx.shortest_path(self.gnx, start.pos(), end.pos())
        except networkx.exception.NetworkXError:
            print("No Path")
            return None
