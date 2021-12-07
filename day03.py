
def grab_list():
    list_of_binaries = []
    with open('03-1-input.txt') as f:
        line = f.readline()
        while line:
            list_of_binaries.append(line)
            line = f.readline()
    f.close()
    #assert(len(list_of_binaries) == 1000)
    return list_of_binaries


def find_power_level(lob, num_size):
    gamma = ''
    epsilon = ''
    for big_loop in range(num_size-1, -1, -1):
        curr1_cnt = 0
        curr0_cnt = 0
        for idx, a_bin in enumerate(lob):
            base10 = int(a_bin,2)
            if base10 >= 2**big_loop:
                curr1_cnt += 1
            else:
                curr0_cnt += 1
            lob[idx] = a_bin[1:]
        if curr1_cnt >= curr0_cnt:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    #print(int(gamma,2) * int(epsilon,2))
    return gamma




def find_life_support(lob, num_size):
    lob_master = lob[:]
    for pos in range(0,num_size):
        lob_copy = lob[:]
        gamma = find_power_level(lob_copy, len(lob_copy[0])-1)
        lob = [x for x in lob if x[pos] == gamma[pos]]
        if (len(lob) == 1):
            break
    oxy = lob[0]

    lob = lob_master[:]
    for pos in range(0,num_size):
        lob_copy = lob[:]
        gamma = find_power_level(lob_copy, len(lob_copy[0])-1)
        epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])
        lob = [x for x in lob if x[pos] == epsilon[pos]]
        if (len(lob) == 1):
            break

    co2 = lob[0]

    print(int(oxy,2) * int(co2,2))

if __name__ == '__main__':
    the_list = grab_list()
    list_copy = the_list[:]
    #gamma = find_power_level(list_copy, len(list_copy[0]) - 1)

    list_copy = the_list[:]
    find_life_support(list_copy, len(list_copy[0]) - 1)