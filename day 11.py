import numpy as np

def flash():
    flash_count = 0
    with open('11-1-input.txt') as f:
        line = np.array([list(x.strip()) for x in f.readlines()])
        line = np.array(line, int)
        line = np.pad(line, pad_width=1, mode='constant', constant_values=0)
        print(line)
        n, m = line.shape
        x, y = np.ogrid[0:n, 0:m]
        for step in range(0,1000):
            full_mask = (x>0)&(x<12)&(y>0)&(y<12)
            line[full_mask] += 1
            any_nines = True
            while any_nines:
                any_nines = False
                for idx in range(1,n-1):
                    for idy in range(1,m-1):
                        if (line[idx][idy] > 9) & (line[idx][idy] < 100):
                            flash_count += 1
                            any_nines = True
                            flash_mask = (x<=idx+1)&(x>=idx-1)&(y<=idy+1)&(y>=idy-1)
                            line[flash_mask] += 1
                            line[idx][idy] = 100
            synchronized = True
            for idx in range(1,n-1):
                for idy in range(1,n-1):
                    if line[idx][idy] >= 100:
                        line[idx][idy] = 0
                    else:
                        synchronized = False
            if (synchronized == True):
                print("sync on step:", step+1)
                break

        print(flash_count)


if __name__ == '__main__':
    flash()