from collections import namedtuple
import numpy as np
from copy import copy, deepcopy

Node = namedtuple("Node", "name cost")
BOUNDARY_COST = 99999
#BOUNDARY_COST = 0
PART_TWO = True
OG_HEIGHT = 0
OG_WIDTH = 0



def bfs_shortest_path():
    pass


def get_neighbors_and_cost(data, in_tuple):

    a_nbor_name = (in_tuple[0],   in_tuple[1]+1)
    b_nbor_name = (in_tuple[0]+1, in_tuple[1])
    c_nbor_name = (in_tuple[0],   in_tuple[1]-1)
    d_nbor_name = (in_tuple[0]-1, in_tuple[1])

    a_nbor = Node(a_nbor_name,data[a_nbor_name])
    b_nbor = Node(b_nbor_name,data[b_nbor_name])
    c_nbor = Node(c_nbor_name,data[c_nbor_name])
    d_nbor = Node(d_nbor_name,data[d_nbor_name])

    return [a_nbor, b_nbor, c_nbor, d_nbor]


def inc_grid(in_grid):
    height, width = in_grid.shape
    out_grid = deepcopy(in_grid)
    for ridx in range(0, height):
        for cidx in range(0, width):
            out_grid[ridx][cidx] = (out_grid[ridx][cidx] % 9) + 1
    return(out_grid)



def test_grid(data):
    for ridx, a_row in enumerate(data):
        for cidx, val in enumerate(a_row):
            if (cidx < (OG_WIDTH*4)):
                assert(data[ridx][cidx+OG_WIDTH] == (data[ridx][cidx] % 9) + 1)
            if (ridx < (OG_HEIGHT*4)):
                assert(data[ridx+OG_HEIGHT][cidx] == (data[ridx][cidx] % 9) + 1)

def inc_large_grid(data):
    out_data = deepcopy(data)
    for ridx, a_row in enumerate(data):
        for cidx, val in enumerate(a_row):
            if (cidx < (OG_WIDTH*4)):
                out_data[ridx][cidx+OG_WIDTH] = (out_data[ridx][cidx] % 9) + 1
            if (ridx < (OG_HEIGHT*4)):
                out_data[ridx+OG_HEIGHT][cidx] = (out_data[ridx][cidx] % 9) + 1
    print(out_data)

    return(out_data)

def build_graph():
    global OG_HEIGHT, OG_WIDTH

    with open('15-1-input.txt') as f:
        data = np.array([[int(y) for y in list(x.strip())] for x in f.readlines()])
        height, width = data.shape
        OG_HEIGHT = height
        OG_WIDTH = width

        if PART_TWO:

            grids = []
            a_grid = deepcopy(data)

            for idx in range(0,4):
                data = np.concatenate((data, a_grid), axis=1)

            a_grid = deepcopy(data)

            for idx in range(0,4):
                data = np.concatenate((data, a_grid), axis=0)

            data = inc_large_grid(data)
            test_grid(data)
            #print(data)

        data = np.pad(data, pad_width=1, mode='constant', constant_values=BOUNDARY_COST)
        calculate_risk(data)

def calculate_risk(data):
    width, height = data.shape
    target_node = (width-2, height-2)

    seen = {}
    visited = []
    current_node = Node((1,1),0)
    data[(1,1)] = 0
    visited.append(current_node.name)
    while current_node.name != target_node:
        nbors = get_neighbors_and_cost(data, current_node.name)
        for nbor in nbors:
            if (nbor.name not in seen.keys()) & (nbor.name not in visited) & (nbor.cost < 9999):
                seen[nbor.name] = current_node.cost + nbor.cost

        new_name = min(seen, key = seen.get)
        new_cost = seen[new_name]
        #print(current_node.name," -> ", new_name, " with cost: ", new_cost, seen)
        print(new_name, new_cost)
        current_node = Node(new_name, new_cost)
        assert(current_node.name not in visited)
        seen.pop(current_node.name)
        visited.append(current_node.name)


    print(current_node.name, current_node.cost)




if __name__ == '__main__':
    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(edgeitems=30, linewidth=100000,
                        formatter=dict(float=lambda x: "%.3g" % x))

    build_graph()