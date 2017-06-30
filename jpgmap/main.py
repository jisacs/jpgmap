#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Implémentation de la proclamation de la bonne parole.

    Usage:

    >>> from sm_lib import proclamer
    >>> proclamer()
"""

from datetime import datetime

__all__ = ['proclamer']

from jpgmap.car import Car
from jpgmap.engine import Engine
from jpgmap.engine import Dir
from jpgmap.road import Road
from jpgmap.map import Map
from jpgmap.map import RGB
from jpgmap.map import PixColor
from jpgmap.map import Pixel

def proclamer():
    """
        Fonction de proclamation de la bonne parole. Aucun paramètre, et
        retourne None, car tout le monde say que "Ex nihilo nihil"
    """
    engine = Engine("raw/small.jpg")
    engine.run()
    """
    map = Map()
    map.load("../raw/small.jpg")
    black = RGB(0, 0, 0)
    x, y = map.find_a_white_pos()
    pixel=Pixel(x,y, black)

    game = Game()
    game.setmap(map)

    #road = Road(pixel)
    #road.find_yourself(map)



    #car = Car(pixel)
    #game.add_car(car)
    """





if __name__ == "__main__":
    proclamer()
