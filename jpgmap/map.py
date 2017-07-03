from scipy.ndimage import imread
#import matplotlib.pyplot as plt
from itertools import chain
import numpy as np

import pygame
from pygame.locals import *

from .road import Road
from .point import Point
from .pixel import Pixel
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

    def init_display(self):
            print("pygame INIT")
            pygame.init()

            self.fenetre = pygame.display.set_mode((640, 480),RESIZABLE)

    def load(self, jpg_filename):
        print("Map load filename: " + jpg_filename)
        if jpg_filename:
            print("load debug")
            self.pixels_color=imread(jpg_filename)
            # self.pixels_color.shape (53, 93, 3)
            self.jpg_filename = jpg_filename
            fond = pygame.image.load(self.jpg_filename).convert()
            self.fenetre.blit(fond, (0,0))
            self.set_pixels_map(self.pixels_color)

            #pygame.surfarray.blit_array(self.fenetre, self.pixels_color)
            pygame.display.flip()
            self.analyse_map()

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
        self.h,self.w,c= pixels_color.shape
        self.pixels_map = [[Pixel(x,y) for y in range(self.h)] for x in range(self.w)]
        #print('self.w {} self.h {}'.format(self.w, self.h))
        for x in range(self.w):
            for y in range(self.h):
                pixel = self.pixels_map[x][y]
                #print("DEBUG ADD Pixel x {}, y {} in tab[{}][{}]".format(pixel.x,pixel.y,x,y))
                if self.is_a_white_pos(pixel, delta=20):
                    pixel.type = Pixel.ROAD
                    #self.fenetre.set_at((x, y), pygame.Color("red"))
                else:
                    pixel.type = Pixel.ROCK
                    #self.fenetre.set_at((x, y), pygame.Color("green"))



        #print('x len {}, y len {}'.format(len(self.pixels_map),len(self.pixels_map[0])))
    def get_pixels_ordered(self):
        """
        return a list order  by x,y -> 0,0 0,1 0,2 0,3 ... 1,0 1,1 1,2
        """
        return list(chain.from_iterable(zip(*self.pixels_map)))


    def analyse_map(self):
        pixels = self.get_pixels_ordered()
        for pixel in pixels:
            neighbours_road, neighbours_road_flags = self.get_neighbours_road(pixel)
            #print(" pixel {} neighbours_road_flags {}".format(pixel, neighbours_road_flags))
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



    def set_pixel(self, pixel):

        self.pixels_color[pixel.y, pixel.x, PixColor.RED.value] = pixel.rgb.red
        self.pixels_color[pixel.y, pixel.x, PixColor.YELLOW.value] = pixel.rgb.yellow
        self.pixels_color[pixel.y, pixel.x, PixColor.BLUE.value] = pixel.rgb.blue


    def get_neighbours(self, pixel):
        result = list()
        neighbours_road_flags = {"UP":False, "DOWN":False, "LEFT":False, "RIGHT":False }
        try:
            p = self.pixels_map[pixel.x+1][pixel.y]
            result.append(p)
            if p.type == Pixel.ROAD:
                neighbours_road_flags["RIGHT"]=True
        except IndexError:
            pass
        try:
            p = self.pixels_map[pixel.x-1][pixel.y]
            result.append(p)
            if p.type == Pixel.ROAD:
                neighbours_road_flags["LEFT"]=True
        except IndexError:
            pass
        try:
            p = self.pixels_map[pixel.x][pixel.y-1]
            result.append(p)
            if p.type == Pixel.ROAD:
                neighbours_road_flags["UP"]=True
        except IndexError:
            pass
        try:
            p=self.pixels_map[pixel.x][pixel.y+1]
            if p.type == Pixel.ROAD:
                neighbours_road_flags["DOWN"]=True
            result.append(p)
        except IndexError:
            pass
        return result, neighbours_road_flags


    def get_neighbours_road(self, pixel):
        result = list()
        neighbours, neighbours_road_flags = self.get_neighbours(pixel)
        for n in neighbours:
            if n.type == Pixel.ROAD:
                result.append(n)
        return result, neighbours_road_flags


    def find_a_white_pos(self):
        for x in range(self.w):
            for y in range(self.h):
                if self.pixels_map[x][y].type == Pixel.ROAD:
                    print("find_a_white_pos x {}, y {}".format(x,y))
                    return self.pixels_map[x][y]


    def is_a_white_pos(self, point, delta=0):
        if self.pixels_color[point.y, point.x, PixColor.RED.value] >= 255 - delta:
            if self.pixels_color[point.y, point.x , PixColor.YELLOW.value] >= 255 - delta  :
                if self.pixels_color[point.y, point.x , PixColor.BLUE.value] >= 255 - delta :
                    return True
        return False


    def display(self):
        for pixel in self.get_pixels_ordered():
            pixel.display(self.fenetre)
        pygame.display.flip()
