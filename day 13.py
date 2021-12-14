import numpy as np


def form_grid():
    rows = []
    columns = []

    with open('13-1-input.txt') as f:
        line = f.readline()
        while line != '\n':
            col, row = line.split(',')
            columns.append(int(col))
            rows.append(int(row))
            line = f.readline()

            width = max(columns) + 1
            height = max(rows) + 1

            grid = np.zeros((height, width))
            for a_col, a_row in zip(columns, rows):
                grid[a_row][a_col] = 1


        line = f.readline()
        while line:
            fold_direction, fold_val = ((line.split(' '))[2]).split('=')
            fold_val = int(fold_val)
            print(fold_direction, fold_val)
            if fold_direction == 'x':
                new_grid = grid[0:height, 0:fold_val]
                to_fold_in = grid[0:height, fold_val+1:width]
                to_fold_in = np.fliplr(to_fold_in)
                width = fold_val
            elif fold_direction == 'y':
                new_grid = grid[0:fold_val, 0:width]
                to_fold_in = grid[fold_val+1:height, 0:width]
                to_fold_in = np.flipud(to_fold_in)
                height = fold_val

            grid = new_grid.copy()
            for rowid, y in enumerate(zip(new_grid,to_fold_in)):
                for colid, x in enumerate(zip(y[0], y[1])):
                    grid[rowid][colid] = x[0] + x[1]
            count = 0
            for idr in range(0, height):
                for idc in range(0, width):
                    if grid[idr][idc] > 0:
                        count += 1
            print("A post-fold count: ", count)


            line = f.readline()

    for idr in range(0, height):
        for idc in range(0, width):
            if grid[idr][idc] > 0:
                grid[idr][idc] = 1
            else:
                grid[idr][idc] = 0
    print(grid)

#RLBCJGLU

if __name__ == '__main__':
    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(edgeitems=30, linewidth=100000,
                        formatter=dict(float=lambda x: "%.3g" % x))
    form_grid()