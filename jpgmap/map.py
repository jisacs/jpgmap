from scipy.ndimage import imread
#import matplotlib.pyplot as plt

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
    def __init__(self):
        self.pixels = None

    def load(self, jpg):
        self.pixels=imread(jpg)
        self.lx, self.ly , self.lz= self.pixels.shape

    def set_pixel(self,x, y, rgb):
        """
        @param x: x coordonate
        @param y: y coordonate
        @param rgb: Object RGB
        """
        self.pixels[x, y, PixColor.RED.value] = rgb.red
        self.pixels[x, y, PixColor.YELLOW.value] = rgb.yellow
        self.pixels[x, y, PixColor.BLUE.value] = rgb.blue

    def find_a_white_pos(self):
        for x in range(self.lx):
            for y in range(self.ly):
                if self.pixels[x, y , PixColor.RED.value] == 255 and self.pixels[x, y , PixColor.YELLOW.value] == 255 and self.pixels[x, y , PixColor.BLUE.value] == 255:
                    return x,y

    """
    def display(self):
        plt.imshow(self.pixels, cmap=plt.cm.gray)
        plt.show()
    """
