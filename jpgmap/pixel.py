import pygame
from pygame.locals import *
from .point import Point

class Pixel():
    UNKNOWN = 0
    ROAD    = 1
    ROCK    = 2

    #ROAD TYPE
    _4     = 0, 0, 0
    _3_UP  = 255, 255, 255
    _3_DO  = 0, 200, 255
    _3_RI  = 255, 0, 0
    _3_LE  = 255, 100, 0
    _2_H   = 0, 255, 0
    _2_V   = 128,128,128
    _2_RD  = 128,0,0
    _2_LD  = 128,0,0
    _2_LU  = 0,128,0
    _2_RU  = 128,0,128
    _1_L   = 0,128,128
    _1_R   = 0,0,128
    _1_D   = 192,192,192
    _1_U   = 0,0,255

    """
    Black 	#000000 	(0,0,0)
  	White 	#FFFFFF 	(255,255,255)
  	Red 	#FF0000 	(255,0,0)
  	Lime 	#00FF00 	(0,255,0)
  	Blue 	#0000FF 	(0,0,255)
  	Yellow 	#FFFF00 	(255,255,0)
  	Cyan / Aqua 	#00FFFF 	(0,255,255)
  	Magenta / Fuchsia 	#FF00FF 	(255,0,255)
  	Silver 	#C0C0C0 	(192,192,192)
  	Gray 	#808080 	(128,128,128)
  	Maroon 	#800000 	(128,0,0)
  	Olive 	#808000 	(128,128,0)
  	Green 	#008000 	(0,128,0)
  	Purple 	#800080 	(128,0,128)
  	Teal 	#008080 	(0,128,128)
  	Navy 	#000080 	(0,0,128)
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    CIEL = 0, 200, 255
    RED = 255, 0, 0
    ORANGE = 255, 100, 0
    GREEN = 0, 255, 0
    """


    def __init__(self, x, y):
        """
        param:
            Point, pixel position
        """
        self.x = x
        self.y = y
        self.type = self.UNKNOWN
        self.road_type = self.UNKNOWN
        #self.neighbours = None

    def __eq__(self, rhs):
        if self.x == rhs.x and self.y == rhs.y:
            return True
        return False

    def __repr__(self):
        return 'x: {}, y: {} type {}'.format(str(self.x), str(self.y),self.type)

    """
    def set_neighbours(self, neighbours):
        self.neighbours = neighbours
        nb_neighbour = 0

        self.set_road_type(neighbours)
        for n in self.neighbours:
            if n.type == self.ROAD:
                nb_neighbour+=1



    def get_neighbours(self):
        return self.neighbours
    """
    """
    def get_nb_neighbour_road(self):
        result = 0
        for n in self.neighbours:
            if n.type == self.ROAD:
                result+=1
        return result
    """

    def display(self, fenetre, offset = Point(0,0))):
        if self.road_type:
            print(self.road_type)
            color = pygame.Color(*self.road_type, 255 )

            fenetre.set_at((self.x+offset.x, self.y+offset.y), color)
