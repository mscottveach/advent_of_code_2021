import numpy as np
line = []

LEFT, RIGHT, UP, DOWN = 1, 2, 3, 4

def calc_risk():
    risk = 0
    global line
    basins = []
    with open('09-1-input.txt') as f:
        line = np.array([list(x.strip()) for x in f.readlines()])
        line = np.array(line, int)
        line = np.pad(line, pad_width=1, mode='constant', constant_values=9)
        row_size, col_size = line.shape
        print(line, row_size, col_size)
        for idr in range(1, row_size-1):
            for idc in range(1, col_size-1):
                if lower_than_neighbors(idr, idc):
                    #print(line[idr][idc])
                    risk += line[idr][idc] + 1

                    basins.append(find_size(idr, idc))

    print(risk)
    basins = sorted(basins,reverse=True)
    print(basins[0] * basins[1] * basins[2])
    return risk

def lower_than_neighbors(idr,idc):
    global line
    # print(idr,idc)
    # print(line,line[idr][idc])
    val = line[idr][idc]
    if val >= line[idr-1][idc]:
        return False
    elif val >= line[idr+1][idc]:
        return False
    elif val >= line[idr][idc+1]:
        return False
    elif val >= line[idr][idc-1]:
        return False

    return True


def find_size(idr, idc):
    global line
    if line[idr][idc] != 9:
        line[idr][idc] = 9
        return(1 + find_size(idr-1,idc) + find_size(idr+1,idc) + find_size(idr,idc-1) + find_size(idr,idc+1))
    else:
        return 0

if __name__ == '__main__':
    calc_risk()