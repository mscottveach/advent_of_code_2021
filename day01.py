



def count_elevation_increases():
    increase_count = 0
    with open('01-1-input.txt') as f:
        lines = f.readline()
        last_val = int(lines)
        lines = f.readline()
        while lines:
            curr_val = int(lines)
            if curr_val > last_val:
                increase_count += 1
            last_val = curr_val
            lines = f.readline()

    f.close()
    return(increase_count)


def count_elev_increase_moving_avg():
    inc_count = 0
    mavgs = []
    with open('01-1-input.txt') as f:
        a_num = int(f.readline())
        b_num = int(f.readline())
        c_num = int(f.readline())
        mavgs.append(a_num+b_num+c_num)
        line = f.readline()
        while line:
            a_num = b_num
            b_num = c_num
            c_num = int(line)
            new_mavg = a_num + b_num + c_num
            if new_mavg > mavgs[-1]:
                inc_count += 1
            mavgs.append(new_mavg)
            line = f.readline()

        return inc_count




if __name__ == '__main__':
    inc_cnt = count_elevation_increases()
    print(inc_cnt)
    inc_cnt = count_elev_increase_moving_avg()
    print(inc_cnt)