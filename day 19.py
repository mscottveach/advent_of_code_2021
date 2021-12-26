import copy
import os
import numpy as np

scanners = {}


rotation_matrix = {'x':[[1,0,0],[0,0,-1],[0,1,0]], 'y':[[0,0,1],[0,1,0],[-1,0,0]], 'z':[[0,-1,0],[1,0,0],[0,0,1]], 'i':[[1,0,0],[0,1,0],[0,0,1]]}
orientations = {}


def gather_scanner_data():
    global scanners

    scanner_cnt = 0
    with open('19-2-input.txt') as f:
        in_line = f.readline().strip()
        beacon_list = []
        while in_line:
            if in_line[0] != '-':
                beacon_list.append(tuple([int(x) for x in in_line.split(',')]))
            in_line = f.readline()
            if in_line in os.linesep:
                scanners[scanner_cnt] = copy.deepcopy(beacon_list)
                scanner_cnt += 1
                beacon_list = []
                in_line = f.readline()

    for key, val in scanners.items():
        print(key, val)


def matrix_mul(a_mat, b_mat):
    a_mat = np.array(a_mat)
    b_mat = np.array(b_mat)

    return np.matmul(a_mat, b_mat)

def rotate_vector(in_vector, rotations, in_axis):
    a_vector = in_vector
    out_vector = [0,0,0]
    a_matrix = rotation_matrix[in_axis]
    for current_rot in range(0,rotations):
        cnt = 0
        for elem in a_vector:
            new_val = 0
            for val in a_matrix[cnt]:
                new_val += elem*val
            out_vector[cnt] = new_val
            cnt += 1
        a_vector = out_vector

    return tuple(out_vector)

def rotate_vector_by_matrix(in_vector, in_rot_mat):
    return np.matmul(in_rot_mat, in_vector)


def build_orientations():
    global orientations
    global rotation_matrix

    count = 0
    orientations[count] = rotation_matrix['i']
    count += 1
    orientations[count] = np.matmul(rotation_matrix['y'], rotation_matrix['y'])
    count += 1
    orientations[count] = rotation_matrix['y']
    count += 1
    orientations[count] = rotation_matrix['z']
    count += 1
    orientations[count] = np.matmul(rotation_matrix['y'], np.matmul(rotation_matrix['y'], rotation_matrix['y']))
    count += 1
    orientations[count] = np.matmul(rotation_matrix['z'], np.matmul(rotation_matrix['z'], rotation_matrix['z']))
    count += 1

    hold_mats = []
    for mat_val in orientations.values():
        new_up = mat_val
        for idx in range(0,3):
            new_up = np.matmul(rotation_matrix['x'],new_up)
            hold_mats.append(new_up)
    for mat in hold_mats:
        orientations[count] = mat
        count += 1

    print(len(orientations))

def check_for_overlap(in_a_scan, in_b_scan):
    global scanners
    global orientations

    for ot in orientations.values():
        hold_a_ot = []
        for elem in in_a_scan:
            hold_a_ot.append(tuple(np.matmul(elem,ot)))

        print(set(hold_a_ot).intersection(in_b_scan))





if __name__ == '__main__':
    test_vec = (1,2,3)
    # print(rotate_vector(test_vec,4,'x'))

    build_orientations()
    # for idx, mat in orientations.items():
    #     print(idx, np.matmul(test_vec, mat))
    gather_scanner_data()
    check_for_overlap(scanners[0],scanners[1])