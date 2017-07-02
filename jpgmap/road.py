from .point import Point
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
            neighbours = _map.get_neighbours(current_pixel)
            print("find_yourself: neighbours" + str(len(neighbours)))
            for search_pixel in neighbours:
                if not search_pixel  in self.pixels:
                    #print("current pos {}, search point {}".format(current_pixel, search_pixel))
                    print("find_yourself: search_pixel x {}, y {}".format(search_pixel.x, search_pixel.y))
                    if _map.is_a_white_pos(search_pixel,delta=10):
                        find = True

                        #print("Add pixel {}".format(search_pixel))
                        self.pixels.append(search_pixel)
                        current_pixel = search_pixel

                        #print("find_yourself: self.pixels {}".format(len(self.pixels)))
                        break
                    else:
                        pass
                    print("find_yourself: find {}".format(find))
                    #print("Not find x={} y={}".format(point.x, point.y))
            #print("find_yourself: All Point Done")
            if not find:
                print("Not find current_pixel {}".format(current_pixel))
                finish = True
            if len(self.pixels) > len(_map.pixels_color):
                finish = True
        print("find_yourself :Stop  nbpixels {}".format(len(self.pixels)))

    def display(self, fenetre):
        #_map = Map(self.blank_map)
        #for car in self.car_list:
        #_map.set_pixel(car.pixel)
        #plt.imshow(_map.pixels, cmap=plt.cm.gray)
        #plt.show()
        #pygame.init
        if fenetre:

            for index, point in enumerate(self.pixels):
                #print(point)
                #print("index {}".format(index))
                if index == 0:
                    color = "blue"
                    fenetre.set_at((point.x, point.y), pygame.Color(color))
                    fenetre.set_at((point.x+1, point.y), pygame.Color(color))
                    fenetre.set_at((point.x-1, point.y), pygame.Color(color))
                    fenetre.set_at((point.x, point.y-1), pygame.Color(color))
                    fenetre.set_at((point.x, point.y+1), pygame.Color(color))

                elif index == len(self.pixels)-1:
                    color = "green"
                    #fenetre.set_at((point.x, point.y), pygame.Color(color))
                else :
                    color = "black"
                    fenetre.set_at((point.x, point.y), pygame.Color(color))
                #print("color {}".format(color))


            #Rafraîchissement de l'écran
            pygame.display.flip()
