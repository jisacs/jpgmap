from scipy.ndimage import imread
#import matplotlib.pyplot as plt
from itertools import chain
import numpy as np

import pygame
from pygame.locals import *

from .road import Road
from .point import Point
from .pixel import Pixel
from .tools import printProgressBar
from .graph import Graph
import networkx
from time import time
import pickle
import  sys



import sys



from enum import Enum
class PixColor(Enum):
    RED = 1
    YELLOW = 2
    BLUE = 0

class RGB():

    def __init__(self,  red, yellow, blue):
        """
        @param red: 0 - 255
        @param yellow: 0 - 255
        @param blue: 0 - 255
        @raise keyError: raises an exception if a value is not 0 - 255
        """
        self.red = red
        self.blue = blue
        self.yellow = yellow


class Map():

    def __init__(self, src=None, jpg_filename=None):
        if src:
            self.pixels_color = np.array(src.pixels)
        else:
            self.pixels_color = None

        self.pixels_map= None
        self.jpg_filename = jpg_filename

        self.fenetre = None
        self.init_display()
        self.roads = list()
        self.zoom = 1
        self.last_display_time = 0
        self.last_display_size_time = 0


        self.graph = None

    def init_display(self):
            print("pygame INIT")
            pygame.init()
            #self.change_display_size(800, 600)


    def load(self, jpg_filename):
        print("Map load filename: " + jpg_filename)
        if jpg_filename:
            self.pixels_color=imread(jpg_filename)
            # self.pixels_color.shape
            self.jpg_filename = jpg_filename
            self.h, self.w, c = self.pixels_color.shape
            self.change_display_size(self.h, self.w)
            self.fond = pygame.image.load(self.jpg_filename).convert()
            self.fenetre.blit(self.fond, (0,0))
            self.set_pixels_map(self.pixels_color)
            #pygame.surfarray.blit_array(self.fenetre, self.pixels_color)
            pygame.display.flip()
            self.analyse_map()
            self.graph = Graph(self)

    def save_pickle(self, filename):
        """
        SAve self.pixel_map to pickled file
        :param filename:

        """
        sys.setrecursionlimit(100000)
        print("eEcusion limit {}".format(sys.getrecursionlimit()))
        print("Dump {} object type of len {}".format(type(self.pixels_map), len(self.pixels_map)))
        with open(filename, 'wb') as handle:
            pickle.dump(self.pixels_map, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load_pickle(self, filename):
        """
        Load self.pixel_map from pickled file
        :param filename:

        """
        with open(filename, 'rb') as handle:
            self.pixels_map = pickle.load(handle)
            self.h = len(self.pixels_map[0])
            self.w = len(self.pixels_map)

            self.fenetre = pygame.display.set_mode((self.w, self.h),
                                                   pygame.RESIZABLE)
            #self.change_display_size(self.h, self.w)
            pygame.display.flip()
            self.graph = Graph(self)


    """
    In [1]: w, h = 8, 5;
    In [2]: Matrix = [[0 for x in range(w)] for y in range(h)]
    In [3]: Matrix
    Out[3]:
    [[0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]]

    In [4]: Matrix[0]
    Out[4]: [0, 0, 0, 0, 0, 0, 0, 0]
    In [6]: Matrix[4]
    Out[6]: [0, 0, 0, 0, 0, 0, 0, 0]
    In [5]: Matrix[5]
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-5-2586e3731bb0> in <module>()
    ----> 1 Matrix[5]

    IndexError: list index out of range

"""


    def set_pixels_map(self, pixels_color):
        self.pixels_map = [[Pixel(x,y) for y in range(self.h)] for x in range(self.w)]
        for x in range(self.w):
            for y in range(self.h):
                pixel = self.pixels_map[x][y]
                if self.is_a_white_pos(pixel, delta=20):
                    pixel.type = Pixel.ROAD
                else:
                    pixel.type = Pixel.ROCK


    def get_pixels_ordered(self):
        """
        return a list order  by x,y -> 0,0 0,1 0,2 0,3 ... 1,0 1,1 1,2
        """
        return list(chain.from_iterable(zip(*self.pixels_map)))

    def get_pixels_road_ordered(self):
        """
        return a list order  by x,y -> 0,0 0,1 0,2 0,3 ... 1,0 1,1 1,2 of
        Pixel ROAD only
        """
        ordered_pixels = list(chain.from_iterable(zip(*self.pixels_map)))
        result = list()
        for pixel in ordered_pixels:
            if pixel.type == Pixel.ROAD:
                result.append(pixel)
        return result

    def analyse_map(self):
        pixels = self.get_pixels_ordered()
        for pixel in pixels:
            if pixel.type == Pixel.ROAD:
                pixel.set_neighours(self.get_neighbours_road(pixel))

    """
    def analyse_map(self):
        pixels = self.get_pixels_ordered()
        nb_pix = len(pixels)
        for index, pixel in enumerate(pixels):
            printProgressBar(index, nb_pix, prefix = 'Analyse map:', suffix = 'Complete', length = 50)
            if pixel.type == Pixel.ROAD:
                neighbours_road = self.get_neighbours_road(pixel)
                neighbours_road_flags = self.get_neighbours_ROAD_flags(pixel)
                if len(neighbours_road) == 1:
                    if neighbours_road_flags["RIGHT"]:
                        pixel.road_type = Pixel._1_R
                    elif neighbours_road_flags["LEFT"]:
                        pixel.road_type = Pixel._1_L
                    elif  neighbours_road_flags["UP"]:
                        pixel.road_type = Pixel._1_U
                    else:
                        pixel.road_type = Pixel._1_D

                elif len(neighbours_road) == 2:
                    if neighbours_road_flags["RIGHT"] and  neighbours_road_flags["LEFT"] :
                        pixel.road_type = Pixel._2_H
                    elif neighbours_road_flags["UP"] and  neighbours_road_flags["DOWN"] :
                        pixel.road_type = Pixel._2_V
                    elif neighbours_road_flags["DOWN"] and  neighbours_road_flags["RIGHT"] :
                        pixel.road_type = Pixel._2_RD
                    elif neighbours_road_flags["DOWN"] and  neighbours_road_flags["LEFT"] :
                        pixel.road_type = Pixel._2_LD
                    elif neighbours_road_flags["UP"] and  neighbours_road_flags["LEFT"] :
                        pixel.road_type = Pixel._2_LU
                    elif neighbours_road_flags["UP"] and  neighbours_road_flags["RIGHT"] :
                        pixel.road_type = Pixel._2_RU

                elif len(neighbours_road) == 3:
                    if neighbours_road_flags["RIGHT"] and  neighbours_road_flags["LEFT"] and  neighbours_road_flags["UP"]:
                        pixel.road_type = Pixel._3_UP
                    elif neighbours_road_flags["RIGHT"] and  neighbours_road_flags["LEFT"] and  neighbours_road_flags["DOWN"]:
                        pixel.road_type = Pixel._3_DO
                    elif neighbours_road_flags["RIGHT"] and  neighbours_road_flags["UP"] and  neighbours_road_flags["DOWN"]:
                        pixel.road_type = Pixel._3_RI
                    else:
                        pixel.road_type = Pixel._3_LE

                elif len(neighbours_road) == 4:
                    pixel.road_type = Pixel._4

                else:
                    pixel.road_type = Pixel._0
                """


    def set_pixel(self, pixel):

        self.pixels_color[pixel.y, pixel.x, PixColor.RED.value] = pixel.rgb.red
        self.pixels_color[pixel.y, pixel.x, PixColor.YELLOW.value] = pixel.rgb.yellow
        self.pixels_color[pixel.y, pixel.x, PixColor.BLUE.value] = pixel.rgb.blue


    def get_all_neighbours(self, pixel):
        """
        Return pixel's neighbour list
        :param pixel:
        :return:
        """
        result = list()
        if pixel.x + 1 < self.w:
            result.append(self.pixels_map[pixel.x+1][pixel.y])

        if pixel.x - 1 >= 0:
            result.append(self.pixels_map[pixel.x-1][pixel.y])

        if pixel.y - 1 >= 0:
            result.append(self.pixels_map[pixel.x][pixel.y-1])

        if pixel.y + 1 < self.h:
            result.append(self.pixels_map[pixel.x][pixel.y+1])

        if pixel.x + 1 < self.w and  pixel.y - 1 >= 0:
            result.append(self.pixels_map[pixel.x+1][pixel.y-1])

        if pixel.x - 1 >= 0  and  pixel.y - 1 >= 0:
            result.append(self.pixels_map[pixel.x-1][pixel.y-1])

        if pixel.y - 1 >= 0 and  pixel.x - 1 :
            result.append(self.pixels_map[pixel.x-1][pixel.y-1])

        if pixel.y + 1 < self.h and  pixel.x - 1 :
            result.append(self.pixels_map[pixel.x-1][pixel.y+1])

        return result

    def get_neighbours_ROAD_flags(self, pixel):
        """
        Return  flags for pixel's neighbour type = ROAD
        :param pixel:
        :return:
        """
        neighbours_road_flags = {"UP":False, "DOWN":False, "LEFT":False, "RIGHT":False }
        if pixel.x + 1 < self.w:
            p = self.pixels_map[pixel.x+1][pixel.y]
            if p.type == Pixel.ROAD:
                neighbours_road_flags["RIGHT"]=True

        if pixel.x - 1 >= 0:
            p = self.pixels_map[pixel.x-1][pixel.y]
            if p.type == Pixel.ROAD:
                neighbours_road_flags["LEFT"]=True

        if pixel.y - 1 >= 0:
            p = self.pixels_map[pixel.x][pixel.y-1]
            if p.type == Pixel.ROAD:
                neighbours_road_flags["UP"]=True
        if pixel.y + 1 < self.h:
            p=self.pixels_map[pixel.x][pixel.y+1]
            if p.type == Pixel.ROAD:
                neighbours_road_flags["DOWN"]=True
        return neighbours_road_flags


    def get_neighbours_road(self, pixel):
        result = list()
        neighbours = self.get_all_neighbours(pixel)
        for n in neighbours:
            if n.type == Pixel.ROAD:
                result.append(n)
        return result



    def find_a_white_pos(self):
        for x in range(self.w):
            for y in range(self.h):
                if self.pixels_map[x][y].type == Pixel.ROAD:
                    return self.pixels_map[x][y]


    def is_a_white_pos(self, point, delta=0):
        if self.pixels_color[point.y, point.x, PixColor.RED.value] >= 255 - delta:
            if self.pixels_color[point.y, point.x , PixColor.YELLOW.value] >= 255 - delta  :
                if self.pixels_color[point.y, point.x , PixColor.BLUE.value] >= 255 - delta :
                    return True
        return False


    def display(self):

        now = time()
        if now - self.last_display_time > .2:
            self.fenetre.fill((0, 0, 0))
            pixels = self.get_pixels_ordered()
            nb_pix = len(pixels)
            for index, pixel in enumerate(pixels):
                printProgressBar(index, nb_pix, prefix = 'Display Pixel:', suffix = 'Complete', length = 40)
                pixel.display(self.fenetre, offset=Point(0, 0), zoom=self.zoom)
            pygame.display.flip()
            print("")
            self.last_display_time = now


    def display_pixel(self, pixel):
        pixel.display(self.fenetre, offset=Point(0, 0), zoom=self.zoom)
        #self.fenetre.blit(self.fond, (0, 0))
        pygame.display.flip()


    def change_display_size(self, w, h):
        now = time()
        # print(now - self.last_display_time)
        if now - self.last_display_size_time > .2:
            self.fenetre = pygame.display.set_mode((w, h),
                                                   pygame.RESIZABLE)
            if self.pixels_map:
                zoom = int((h) / len(self.pixels_map[0]))
                zoom_z = int((w) / len(self.pixels_map))
                if zoom_z < zoom: zoom = zoom_z
                #print('w {}, h {}, min {}, compare {}'.format(w, h, min, compare))

                self.zoom = zoom
                if self.zoom < 2: self.zoom = 2
                #print("zoom {}".format(self.zoom ))
                pygame.display.flip()
            self.last_display_size_time = now



    def click(self, x, y):

        try:
            pixel = self.pixels_map[x][y]
            if pixel.type == Pixel.ROAD:
                if pixel.selected:
                    pixel.selected = False
                    pixel.cross = True
                elif pixel.cross:
                    pixel.start = True
                    pixel.cross = False
                elif pixel.start:
                    pixel.start = False
                else:
                    pixel.selected = True

                self.display_pixel(pixel)
                selected = list()
                for pixel in self.get_pixels_road_ordered():
                    if pixel.selected:
                        selected.append(pixel)
                ## START PATH FIND
                if len(selected) == 2:
                    try:
                        path = self.graph.get_paths(selected)
                        if path:
                            for points in path:
                                self.pixels_map[points[0]][points[1]].selected = True
                                self.display_pixel(self.pixels_map[points[0]][points[1]])
                    except networkx.exception.NetworkXNoPath:
                        pass
        except IndexError:
            pass


    def unselected(self, pixels=None):

        if not pixels:
            self.unselect_all_pixel()
        else:
            for pixel in pixels:
                pixel.selected=False
                self.display_pixel(pixel)


    def get_selected_pixels(self):
        selected = list()
        for pixel in self.get_pixels_road_ordered():
            if pixel.selected:
                selected.append(pixel)
        return selected


    def unselect_all_pixel(self):
        for pixel in self.get_selected_pixels():
            pixel.selected=False
            self.display_pixel(pixel)