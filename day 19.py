import copy
import os
import numpy as np

scanners = {}
scanner_pos = {}

rotation_matrix = {'x':[[1,0,0],[0,0,-1],[0,1,0]], 'y':[[0,0,1],[0,1,0],[-1,0,0]], 'z':[[0,-1,0],[1,0,0],[0,0,1]], 'i':[[1,0,0],[0,1,0],[0,0,1]]}
orientations = {}


def gather_scanner_data():
    global scanners

    scanner_cnt = 0
    with open('19-1-input.txt') as f:
        in_line = f.readline().strip()
        beacon_list = []
        while in_line:
            if in_line[1] != '-':
                beacon_list.append(tuple([int(x) for x in in_line.split(',')]))
            in_line = f.readline()
            if in_line in os.linesep:
                scanners[scanner_cnt] = copy.deepcopy(beacon_list)
                scanner_cnt += 1
                beacon_list = []
                in_line = f.readline()

    for key, val in scanners.items():
        print(key, val)
    print('')
    print('******')
    print('')


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
    global scanner_pos
    scanner_pos[0] = (0,0,0)
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



def check_for_overlap(in_a_scan, in_b_scan, scan_num_to_check):
    global scanners
    global orientations

    found_match = 0
    for ot in orientations.values():
        hold_b_ot = []
        for elem in in_b_scan:
            hold_b_ot.append(tuple(np.matmul(elem,ot)))
        found_match = align_matrices(in_a_scan, hold_b_ot, scan_num_to_check)
        if found_match:
            break
    if found_match:
        for idx, val in scanner_pos.items():
            print(f'Scanner {idx} is at {val}.')

    return found_match

def align_matrices(in_a, in_b, scan_num_to_check):
    global scanner_pos
    global scanners

    found_match = False
    for b_elem in in_b:
        for a_elem in in_a:
            copy_b = copy.deepcopy(in_b)
            copy_a = copy.deepcopy(in_a)
            # get the difference between a_elem and b_elem
            convert_sum = np.subtract(a_elem, b_elem)

            #if b_elem == (686,422,578):
                #print(a_elem, b_elem)

            # apply difference to all of copy_a
            for idx, beacon in enumerate(copy_b):
                copy_b[idx] = tuple(np.add(beacon,convert_sum))

            # compare copy_a to copy_b and store matches in shared_beacons
            hold_matches = set(copy_b).intersection(set(copy_a))
            # if len(shared_beacons) >= 12, add all of modified a beacons to in_b (i should switch a and b as inputs)
            if len(hold_matches) >= 12:
                found_match = True
                break

            # that works ^^^ so now, I need to calculate the absolute location of scanner b
            # update all of scanner b's beacons into their absolute position
            # put copy of scanner b absolute location and absolute beacons to the side
            # add absolute beacon positions to scanner a and start the entire process over.
        b_count = 0
        if found_match:
            scanner_pos[scan_num_to_check] = tuple(convert_sum)
            for elem in copy_b:
                if elem not in scanners[0]:
                    scanners[0].append(elem)
                    b_count += 1
            break


    return found_match


if __name__ == '__main__':
    test_vec = (1,2,3)
    # print(rotate_vector(test_vec,4,'x'))

    build_orientations()
    # for idx, mat in orientations.items():
    #     print(idx, np.matmul(test_vec, mat))
    gather_scanner_data()
    print('Scanner 0 length is ', len(scanners[0]))

    #this makes a list of scanners that need to be checked against 0
    scanners_left_to_check = []
    for a_key in scanners.keys():
        if (a_key != 0):
            scanners_left_to_check.append(a_key)

    while len(scanners_left_to_check) > 0:
        idx = scanners_left_to_check.pop(0)
        if not check_for_overlap(scanners[0],scanners[idx],idx):
           scanners_left_to_check.append(idx)


    print(len(scanners[0]))
    print(scanner_pos)
    num_of_scanners = len(scanner_pos)
    max_dist = 0
    for idx in range(0, num_of_scanners-1):
        for idx2 in range(idx+1,num_of_scanners):
            tup_dist = tuple(np.subtract(scanner_pos[idx],scanner_pos[idx2]))
            m_dist = [abs(x) for x in list(tup_dist)]
            m_dist = sum(m_dist)
            if m_dist > max_dist:
                max_dist = m_dist

    print(max_dist)