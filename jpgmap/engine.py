import numpy as np
from .map import RGB
from .map import Map
from .map import Point
import pygame
from pygame.locals import *
from enum import Enum
import sys


class Dir(Enum):
    SOUTH = 0
    NORTH = 1
    EAST = 2
    WEST = 3


class Engine():
        def __init__(self, filename,  output=None):
            """
            param image_filename: str image file name
            """

            self.blank_map = None
            self.car_list = list()
            print("Engine filename [{}]".format(filename))
            self.map = Map()

            if filename.find('.jpgmap') != -1:
                self.map.load_pickle(filename)

            else:
                self.map.load(filename)
                self.map.save_pickle(output)
                print("Done -> {}".format(output))
                sys.exit()





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
                    elif  event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.map.zoom*=2
                            self.map.display()
                        elif event.key == pygame.K_DOWN:
                            self.map.zoom/=2
                            self.map.display()
                        elif event.key == pygame.K_SPACE:
                            self.map.unselected()


                        if self.map.zoom < 0: self.map.zoom = 1


                    elif event.type == VIDEORESIZE:

                        if event.w != self.map.w or event.h != self.map.h:
                            print("(event.w {}, event.h {})".format(event.w, event.h))
                            self.map.change_display_size(event.w, event.h)
                            self.map.display()


                    elif event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        self.map.click(int(pos[0]/self.map.zoom), int(pos[1]/self.map.zoom))
