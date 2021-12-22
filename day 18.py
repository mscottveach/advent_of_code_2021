






def snail_add(in_left, in_right):
    result = '[' + in_left +','+in_right+']'
    return result


def get_num_pair(in_num, idx):
    res_s = ''
    res_r = ''
    while in_num[idx].isnumeric():
        res_s += in_num[idx]
        idx += 1
    idx += 1
    while in_num[idx].isnumeric():
        res_r += in_num[idx]
        idx += 1
    return int(res_s), int(res_r)

def snail_explode(in_num):
    lhbs = []
    count = 0
    for idx, c in enumerate(in_num):
        if (count >= 5) & (c == '['):
            lhx, rhx = get_num_pair(in_num,idx+1)
        if c == '[':
            count += 1
        elif c == ']':
            count -= 1
            lhc = lhbs.pop()
            while lhc != '[':
                lhc = lhbs.pop()

        lhbs.append(c)


if __name__ == '__main__':
    test_num = '[[[[[9,8],1],2],3],4]'
    #snail_explode(test_num)
    print(get_num(test_num,5))