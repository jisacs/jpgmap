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
            print("Engine filename [{}]".format(image_filename))
            self.map = Map()
            self.map.load(image_filename)

        def setmap(self, _map):
            self.blank_map = _map

        def add_car(self, car):
            self.car_list.append(car)

        def run(self):
            self.map.display()
            continuer = True
            #Boucle infinie
            while continuer:
                for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
                    if event.type == QUIT:     #Si un de ces événements est de type QUIT
                        continuer = 0      #On arrête la boucle
                    else:
                        self.map.display()
