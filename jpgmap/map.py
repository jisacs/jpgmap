from scipy.ndimage import imread
#import matplotlib.pyplot as plt
import numpy as np
import pygame
from pygame.locals import *


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

class Point():
    def __init__(self, x , y):
        self.x = x
        self.y = y

class Pixel(Point):
    def __init__(self, x , y, rgb):
        self.x = x
        self.y = y
        self.rgb = rgb

class Map():

    def __init__(self, src=None, jpg_filename=None):
        if src:
            self.pixels = np.array(src.pixels)
        else:
            self.pixels = None

        self.jpg_filename = jpg_filename

    def load(self, jpg_filename):
        self.pixels=imread(jpg_filename)
        self.jpg_filename = jpg_filename
        self.lx, self.ly , self.lz= self.pixels.shape

    def set_pixel(self, pixel):
        """
        @param pixel: Pixel(x, y, rgb)
        """
        self.pixels[pixel.x, pixel.y, PixColor.RED.value] = pixel.rgb.red
        self.pixels[pixel.x, pixel.y, PixColor.YELLOW.value] = pixel.rgb.yellow
        self.pixels[pixel.x, pixel.y, PixColor.BLUE.value] = pixel.rgb.blue

    def find_a_white_pos(self):
        for x in range(self.lx):
            for y in range(self.ly):
                if self.pixels[x, y , PixColor.RED.value] == 255 and self.pixels[x, y , PixColor.YELLOW.value] == 255 and self.pixels[x, y , PixColor.BLUE.value] == 255:
                    return x,y


    def is_a_white_pos(self, point, delta=0):


        #print("is_a_white_pos RED {}".format(self.pixels[point.x, point.y, PixColor.RED.value]))
        #print("is_a_white_pos YELLOW {}".format(self.pixels[point.x, point.y, PixColor.YELLOW.value]))
        #print("is_a_white_pos BLUE {}".format(self.pixels[point.x, point.y, PixColor.BLUE.value]))

        if self.pixels[point.x, point.y, PixColor.RED.value] >= 255 - delta:
            if self.pixels[point.x, point.y , PixColor.YELLOW.value] >= 255 - delta  :
                if self.pixels[point.x, point.y , PixColor.BLUE.value] >= 255 - delta :
                    return True
        return False

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
        if self.jpg_filename:
            print(self.jpg_filename)
            fond = pygame.image.load(self.jpg_filename).convert()
            fenetre.blit(fond, (0,0))

        fenetre.set_at((10, 10), pygame.Color("red"))
        #Rafraîchissement de l'écran
        pygame.display.flip()
