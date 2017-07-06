import pygame
from pygame.locals import *
from .point import Point

class Pixel():
    UNKNOWN = "UNKNOWN"
    ROAD    = "ROAD"
    ROCK    = "ROCK"

    #ROAD TYPE

    _0     = "_0"
    _4     = "_4"
    _3_UP  = "_3_UP"
    _3_DO  = "_3_DO"
    _3_RI  = "_3_RI"
    _3_LE  = "_3_LE"
    _2_H   = "_2_H"
    _2_V   = "_2_V"
    _2_RD  = "_2_RD"
    _2_LD  = "_2_LD"
    _2_LU  = "_2_LU"
    _2_RU  = "_2_RU"
    _1_L   = "_1_L"
    _1_R   = "_1_R"
    _1_D   = "_1_D"
    _1_U   = "_1_U"
    #ROAD TYPE



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
        self.selected = False


    def __eq__(self, rhs):
        if self.x == rhs.x and self.y == rhs.y:
            return True
        return False

    def __repr__(self):

        return 'x: {}, y: {} type {} road  type {}'.format(str(self.x),
        str(self.y), self.type, self.road_type)

    def pos(self):
        return self.x, self.y
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

    def display(self, fenetre, offset = Point(0,0),zoom = 10):
        colors = {
        self._0     : (0,0,0),

        self._4     : (255,0,0),
        # BLEU
        self._3_UP  : (0, 0, 255),
        self._3_DO  : (0, 0, 255),
        self._3_RI  : (0, 0, 255),
        self._3_LE  : (0, 0, 255),
        # GREEN
        self._2_H   : (0,255,10),
        self._2_V   : (0,255,20),
        self._2_RD  : (0,255,30),
        self._2_LD  : (0,255,40),
        self._2_LU  : (0,255,50),
        self._2_RU  : (0,255,60),
        # WHITE
        self._1_L   : (255,255,255),
        self._1_R   : (255,255,255),
        self._1_D   : (255,255,255),
        self._1_U   : (255,255,255)
        }

        if self.type == self.ROAD:
            #color = pygame.Color(*colors[self.road_type], 255 )
            color = pygame.Color("white")
        elif self.type == self.ROCK:
            color = pygame.Color("grey")
            #print(self.road_type)
        if self.selected:
            color = pygame.Color("black")
        x = self.x * zoom
        y = self.y * zoom


        for i in range(zoom):
            for j in range(zoom):
                if i == 0 or j == 0:
                    fenetre.set_at((x+offset.x+i, y+offset.y+j), pygame.Color("black"))
                else:
                    fenetre.set_at((x+offset.x+i, y+offset.y+j), color)
