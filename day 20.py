import numpy as np


enhance_image = {}
the_image = []

def read_image():
    global the_image
    global enhance_image

    with open('20-1-input.txt') as f:
        line = f.readline()
        count = 0
        for elem in line:
            enhance_image[count] = elem
            count += 1
        f.readline()
        the_image = np.array([[x for x in line.strip()] for line in f])


def calc_pixel_score(in_x, in_y, in_image):
    stor_pixels = []

    x = in_x - 1
    y = in_y - 1

    for idy in range(0,3):
        for idx in range(0,3):
            stor_pixels.append(in_image[idy+y][idx+x])

    bin_string = ''
    for elem in stor_pixels:
        if elem == '.':
            bin_string += '0'
        elif elem == '#':
            bin_string += '1'
    the_score = int(bin_string,2)

    return the_score



def process_image(in_image):
    global enhance_image

    x, y = in_image.shape
    #print(x,y)
    new_image = np.copy(in_image)
    for idx in range(1, x-1):
        for idy in range(1,y-1):
            a_score = calc_pixel_score(idx, idy, in_image)
            new_image[idy][idx] = enhance_image[a_score]

    return new_image

if __name__ == '__main__':
    np.set_printoptions(edgeitems=30, linewidth=100000,
                        formatter=dict(float=lambda x: "%.3g" % x))
    read_image()
    procd = np.pad(the_image, pad_width=200, mode='constant', constant_values='.')

    for idx in range(0,50):
        procd = process_image(procd)

    procd = procd[120:-120,120:-120]
    print(procd)

    count = 0
    for row in procd:
        for elem in row:
            if elem == '#':
                count += 1
    print(count)