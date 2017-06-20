import numpy as np
from .map import RGB
from .map import Map
import matplotlib.pyplot as plt

from enum import Enum
class Dir(Enum):
    SOUTH = 0
    NORTH = 1
    EAST = 2
    WEST = 3


class Game():
        def __init__(self):
            self.blank_map = None
            self.car_list = list()

        def setmap(self, _map):
            self.blank_map = _map

        def add_car(self, car):
            self.car_list.append(car)

        def display(self):
            _map = Map(self.blank_map)
            for car in self.car_list:
                _map.set_pixel(car.pixel)
            plt.imshow(_map.pixels, cmap=plt.cm.gray)
            plt.show()


class Car():
    def __init__(self, pixel):
        self.pixel=pixel
        self.direction = Dir.SOUTH.value

    def move(self):
        if self.direction == Dir.SOUTH.value:
            self.pixel.x+=10
        if self.direction == Dir.NORTH.value:
            self.pixel.x-=10
        if self.direction == Dir.EAST.value:
            self.pixel.y+=10
        if self.direction == Dir.WEST.value:
            self.pixel.y-=10
        print(self.direction)
