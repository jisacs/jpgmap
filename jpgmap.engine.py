import numpy as np
from .map import RGB
from .map import Map
from .map import Point
import pygame
from pygame.locals import *

from enum import Enum
class Dir(Enum):
    SOUTH = 0
    NORTH = 1
    EAST = 2
    WEST = 3


class Engine():
        def __init__(self, image_filename=None):
            """
            param image_filename: str image file name
            """

            self.blank_map = None
            self.car_list = list()
            self.image_filename = image_filename
            print("Engine filename [{}]".format(image_filename))

        def setmap(self, _map):
            self.blank_map = _map

        def add_car(self, car):
            self.car_list.append(car)

        def run(self):
            pass


        def display(self):
            #_map = Map(self.blank_map)
            #for car in self.car_list:
            #_map.set_pixel(car.pixel)
            #plt.imshow(_map.pixels, cmap=plt.cm.gray)
            #plt.show()
            #pygame.init
            print("pygame INIT")
            pygame.init()

            fenetre = pygame.display.set_mode((640, 480),RESIZABLE)
            if self.image_filename:
                print(self.image_filename)
                fond = pygame.image.load(self.image_filename).convert()
            fenetre.blit(fond, (0,0))
            #Rafraîchissement de l'écran
            pygame.display.flip()
            cont = True
            while cont:

                   continue

class Road():
    def __init__(self,point):
        self.start = point
        self.pixels=[self.start]

    def find_yourself(self, _map):
        print("DEBUG")
        finish = False
        while not finish:
            find = False
            pt = self.pixels[-1]
            search=[Point(pt.x+1,pt.y), Point(pt.x,pt.y-1), Point(pt.x-1,pt.y),
            Point(pt.x,pt.y+1)]
            for point in search:
                if _map.is_a_white_pos(point,delta=10) and not point in self.pixels:
                    find = True
                    #print("find x={} y={}".format(point.x, point.y))
                    self.pixels.append(pt)
                    break
                else:
                    pass
                    #print("Not find x={} y={}".format(point.x, point.y))

            if not find:
                finish = True






class Car():
    def __init__(self, pixel):
        self.pixel=pixel
        self.direction = Dir.SOUTH.value
