from .pixel import Pixel
import pygame


class Road():
    def __init__(self,pixel ):
        self.start = pixel
        self.pixels=[self.start]  #List of Pixel


    def find_yourself(self, _map):
        print("find_yourself :Start ")
        voisins={}
        finish = False
        current_pixel = self.pixels[0]
        print("find_yourself :first x {} , y {} ".format(current_pixel.x, current_pixel.y))
        while not finish:
            find = False
            step = 1
            #search=[Pixel(current_pixel.x+step,current_pixel.y), Pixel(current_pixel.x,current_pixel.y-step),
             #Pixel(current_pixel.x-step,current_pixel.y), Pixel(current_pixel.x,current_pixel.y+step)]

            neighbours = current_pixel.get_neighbours()
            #print("find_yourself: neighbours" + str(len(neighbours)))
            for search_pixel in neighbours:
                if not search_pixel  in self.pixels:
                    #print("current pos {}, search pixel {}".format(current_pixel, search_pixel))
                    #print("find_yourself: search_pixel x {}, y {}".format(search_pixel.x, search_pixel.y))
                    if _map.is_a_white_pos(search_pixel,delta=10):
                        find = True
                        #print("Add pixel {}".format(search_pixel))
                        self.pixels.append(search_pixel)
                        #print("current_pixel - next x {}, y {}".format(search_pixel.x-current_pixel.x,search_pixel.y-current_pixel.y))
                        current_pixel = search_pixel
                        #print("find_yourself: self.pixels {}".format(len(self.pixels)))
                        break
                    else:
                        pass
                    #print("find_yourself: find {}".format(find))
                    #print("Not find x={} y={}".format(pixel.x, pixel.y))
            #print("find_yourself: All Point Done")
            if not find:
                print("Not find current_pixel {}".format(current_pixel))
                finish = True
            if len(self.pixels) > _map.pixels_color.size:
                print("len(self.pixels) {} > len(_map.pixels_color): {}".format(len(self.pixels), len(_map.pixels_color)))
                finish = True
        print("find_yourself :Stop  nbpixels {}".format(len(self.pixels)))

    
