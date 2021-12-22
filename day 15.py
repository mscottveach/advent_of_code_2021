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

# def get_min_next_step(tpq):
#     next_step_weights = list(zip(*tpq))[1]
#     min_step = min(next_step_weights)
#     min_step_idx = next_step_weights.index(min_step)
#     curr_node = tpq[min_step_idx]
#     tpq.pop(min_step_idx)
#     return curr_node


# def check_node_cost(tpq, name):
#     node_idx = (list(zip(*tpq))[0]).index(name)
#     node_cost = tpq[node_idx].cost
#     return node_cost, node_idx


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

            # for idx in range(0,4):
            #     a_grid = inc_grid(a_grid)
            #     grids.append(a_grid)
            #     #print(a_grid)
            #
            # print("Entering concat...")
            # for a_grid in grids:
            #     data = np.concatenate((data,a_grid),axis=1)
            #
            # a_grid = deepcopy(data)
            # for idx in range(0,4):
            #     a_grid = inc_grid(a_grid)
            #     data = np.concatenate((data,a_grid),axis=0)

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



# def calc_risk(data, height, width):
#
#     tpq = []
#     starting_node = Node((1,1),0,[(1,1)])
#     tpq.append(starting_node)
#     while (height,width) not in list(zip(*tpq))[0]:
#
#         curr_node = get_min_next_step(tpq)
#         nbors = get_neighbors(curr_node.name)
#         print(curr_node.cost, len(curr_node.path))
#         for nbor in nbors:
#
#             cost_to_enter = data[nbor]
#             if cost_to_enter == BOUNDARY_COST:
#                 continue
#             new_list = curr_node.path.copy()
#             new_list.append(nbor)
#             new_node = Node(nbor, cost_to_enter + curr_node.cost, new_list)
#
#             if not tpq:
#                 tpq.append(new_node)
#             elif (nbor not in list(zip(*tpq))[0]) and (nbor not in curr_node.path):
#                 tpq.append(new_node)
#             elif nbor in list(zip(*tpq))[0]:
#                 existing_cost, existing_cost_idx = check_node_cost(tpq, nbor)
#                 if existing_cost > (cost_to_enter + curr_node.cost):
#                     tpq.pop(existing_cost_idx)
#                     tpq.append(new_node)
#
#     calc_path = curr_node.path
#     final_path = ''
#     total_risk = 0
#     for pos in calc_path:
#         total_risk += data[pos]
#         final_path += str(data[pos])
#     total_risk -= data[(1,1)]
#     total_risk += data[(height,width)]
#     final_path += str(data[(height,width)])
#     print(total_risk, final_path)
#
# def flow_risk(data, starting_node):
#     print(data)
#     height, width = data.shape
#     for ridx in range(1, height-1):
#         for cidx in range(1, width-1):
#             left_val = data[ridx][cidx-1]
#             top_val = data[ridx-1][cidx]
#             right_val = data[ridx][cidx+1]
#             bot_val = data[ridx+1][cidx]
#             prop_val = min(left_val,top_val,right_val,bot_val)
#             data[ridx][cidx] += prop_val
#             print(ridx, cidx, left_val, top_val, data[ridx][cidx])
#
#     print(data[width-2][height-2] - data[1][1])




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