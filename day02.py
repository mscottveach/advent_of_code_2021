




def calc_pos():
    for_pos = 0
    dep_pos = 0
    with open('02-1-input.txt') as f:
        line = f.readline()
        while line:
            command = line.split(' ')
            if command[0] == 'forward':
                for_pos += int(command[1])
            if command[0] == 'up':
                dep_pos -= int(command[1])
            if command[0] == 'down':
                dep_pos += int(command[1])
            line = f.readline()

    print('Forward position is ',for_pos)
    print('Depth position is ', dep_pos)
    print('Their product is', for_pos * dep_pos)


def calc_pos_with_aim():
    for_pos = 0
    dep_pos = 0
    aim = 0
    with open('02-1-input.txt') as f:
        line = f.readline()
        while line:
            command = line.split(' ')
            if command[0] == 'forward':
                for_pos += int(command[1])
                dep_pos += aim * int(command[1])
            if command[0] == 'up':
                aim -= int(command[1])
            if command[0] == 'down':
                aim += int(command[1])
            line = f.readline()

    print('Forward position is ',for_pos)
    print('Depth position is ', dep_pos)
    print('Their product is', for_pos * dep_pos)


if __name__ == '__main__':
    calc_pos()
    calc_pos_with_aim()
