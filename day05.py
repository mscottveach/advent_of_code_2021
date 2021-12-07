
import numpy as np

class Grid():

    def __init__(self, size):
        self.the_lines = []
        self.size = size
        self.the_grid = np.zeros([size+1, size+1], np.int32, order='F')

            #print("a grid: ",the_grid)

    def test_grid(self):
        self.the_grid[(3, 3)] = 5

    def add_line(self, a_line):
        self.the_lines.append(a_line)
        self.the_grid[a_line.point_a()] += 1
        print(a_line.point_a())
        self.the_grid[a_line.point_b()] += 1
        for a_point in a_line.get_internal_points():
            self.the_grid[a_point] += 1

    def add_udline(self, aline):
        if aline.m == 0:
            self.add_line(aline)

    def print_grid(self):
        np.set_printoptions(threshold=np.sys.maxsize)
        self.the_grid = self.the_grid.transpose()
        print(self.the_grid)

    def count_overlap(self):
        count = 0
        for i in range(0,self.size+1):
            for j in range(0,self.size+1):
                if self.the_grid[i][j] >= 2:
                    count += 1
        print(count)

class Line():

    def __init__(self, point_a, point_b):
        self.m_flag = True
        self.a = point_a
        self.b = point_b
        if (point_b[0] - point_a[0]) != 0:
            self.m = (point_b[1] - point_a[1])/(point_b[0] - point_a[0])
        else:
            self.m = 0
            self.m_flag = False

        self.q = point_b[1] - self.m*point_b[0]
        self.internal_points = []
        self.calc_internal_points()
        print(point_a,point_b,self.internal_points)

    def calc_internal_points(self):
        if self.m_flag:
            for an_x in range(min(self.x_vals())+1, max(self.x_vals())):
                a_y = self.m*an_x + self.q

                if a_y.is_integer():
                    self.internal_points.append((an_x,int(a_y)))
        else:
            for a_y in range(min(self.y_vals())+1, max(self.y_vals())):
                self.internal_points.append((self.point_a()[0],a_y))


    def get_internal_points(self):
        return self.internal_points

    def x_vals(self):
        return([self.a[0], self.b[0]])

    def y_vals(self):
        return([self.a[1], self.b[1]])

    def point_a(self):
        return self.a

    def point_b(self):
        return self.b

    def print_line(self):
        print(self.a, " -> ", self.b)

    def max_val(self):
        return max([max(self.a),max(self.b)])

def someting():
    track_maxes = []
    the_lines = []
    with open('05-1-input.txt') as f:
        line = f.readline()
        while line:
            a_line = (line.strip()).split(' -> ')
            point_a = tuple([int(x) for x in (a_line[0].split(','))])
            point_b = tuple([int(x) for x in (a_line[1].split(','))])
            print(point_a, point_b)
            the_line = Line(point_a,point_b)
            track_maxes.append(the_line.max_val())
            the_lines.append(the_line)

            line = f.readline()

    a_grid = Grid(max(track_maxes))
   # a_grid.test_grid()
    #a_grid.print_grid()
    for a_line in the_lines:
        a_grid.add_line(a_line)

    a_grid.print_grid()
    a_grid.count_overlap()


if __name__ == '__main__':
    someting()