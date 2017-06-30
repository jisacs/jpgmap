class Road():
    def __init__(self,point):
        self.start = point
        self.pixels=[self.start]

    def find_yourself(self, _map):
        print("DEBUG")
        finish = False
        while not finish:
            find = False
            pt = self.pixels[-1]
            search=[Point(pt.x+1,pt.y), Point(pt.x,pt.y-1), Point(pt.x-1,pt.y),
            Point(pt.x,pt.y+1)]
            for point in search:
                if _map.is_a_white_pos(point,delta=10) and not point in self.pixels:
                    find = True
                    #print("find x={} y={}".format(point.x, point.y))
                    self.pixels.append(pt)
                    break
                else:
                    pass
                    #print("Not find x={} y={}".format(point.x, point.y))

            if not find:
                finish = True
