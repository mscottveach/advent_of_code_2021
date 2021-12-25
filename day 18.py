
import math
import copy



def str_to_num(in_str):
    out_eq = []
    hold_num = ''
    for c in in_str:
        if c.isnumeric():
            hold_num += c
        elif len(hold_num) > 0:
            out_eq.append(int(hold_num))
            hold_num = ''
            out_eq.append(c)
        else:
            out_eq.append(c)

    out_eq = [x for x in out_eq if x != ',']
    return out_eq

def print_eq(in_eq):
    str_eq = [str(x) for x in in_eq]
    print(''.join(str_eq))
    print('')

def snail_explode(in_num):
    working_stack = []
    nst_cnt = 0
    prev_num_idx = 0
    next_num_idx = 0
    found_xploded = False
    skip = False
    for idx in range(0,len(in_num)):
        val = in_num[idx]
        if skip:
            skip = False
        elif val == '[':
            nst_cnt += 1
            working_stack.append(val)
        elif val == ']':
            nst_cnt -= 1
            working_stack.append(val)
        elif (isinstance(val, int)) & (nst_cnt < 5) & (not found_xploded):
            prev_num_idx = len(working_stack)
            working_stack.append(val)
        elif (isinstance(val, int)) & (isinstance(in_num[idx+1],int)) & (nst_cnt >= 5) & (not found_xploded):
            found_xploded = True
            #grab exploding values
            lh_val = val
            rh_val = in_num[idx+1]
            # jump idx to closing bracked
            skip = True
            # store current position in stack
            xploding_idx = len(working_stack) - 1
        elif (isinstance(val, int)) & (found_xploded):
            if next_num_idx == 0:
                next_num_idx = idx - 2
            working_stack.append(val)
        else:
            working_stack.append(val)

    if found_xploded:
        working_stack.pop(xploding_idx)
        working_stack.pop(xploding_idx)
        next_num_idx -= 2
        working_stack.insert(xploding_idx, 0)
        next_num_idx += 1
        if next_num_idx < 0:
            next_num_idx = 0
        if prev_num_idx != 0:
            working_stack[prev_num_idx] += lh_val
        if next_num_idx != 0:
            working_stack[next_num_idx] += rh_val

    return working_stack, found_xploded

def snail_split(in_num):
    working_stack = []
    found_split = False
    for elem in in_num:
        working_stack.append(elem)
        if (isinstance(elem,int)) & (not found_split):
            if elem >= 10:
                found_split = True
                working_stack.pop()
                working_stack.append('[')
                #print('Splitting: ',elem)
                working_stack.append(math.floor(elem/2))
                working_stack.append(math.ceil(elem/2))
                working_stack.append(']')

    #print_eq(working_stack)
    return working_stack, found_split

def calc_mag(in_eq):
    working_eq = copy.deepcopy(in_eq)
    lft_num = []
    rgt_num = []
    if len(working_eq) == 1:
        return working_eq[0]
    else:
        working_eq.pop(0)
        working_eq.pop()
        lft_cnt = 1
        lft_num.append(working_eq.pop(0))
        if isinstance(lft_num[0], int):
            working_on_left = False
        else:
            working_on_left = True
        for c in working_eq:
            if working_on_left == True:
                lft_num.append(c)
            else:
                rgt_num.append(c)
            if c == '[':
                lft_cnt += 1
            elif c == ']':
                lft_cnt -= 1
            if lft_cnt == 0:
                working_on_left = False
        return 3*calc_mag(lft_num) + 2*calc_mag(rgt_num)

def snail_add(curr_eq, next_eq):
    eq_to_simplify = ['['] + curr_eq + next_eq + [']']
    analyze_num = True
    while analyze_num:
        did_xplode = False
        did_split = False
        eq_to_simplify, did_xplode = snail_explode(eq_to_simplify)
        if not did_xplode:
            eq_to_simplify, did_split = snail_split(eq_to_simplify)
        if did_xplode | did_split:
            analyze_num = True
        else:
            analyze_num = False
    return eq_to_simplify

def process_input():
    with open('18-1-input.txt') as f:
        num1 = f.readline().strip()
        curr_eq = str_to_num(num1)
        next_num = f.readline().strip()
        while next_num:
            next_eq = str_to_num(next_num)
            curr_eq = snail_add(curr_eq, next_eq)
            next_num = f.readline().strip()

    print(calc_mag(curr_eq))

def find_largest_magnitude():
    count = 0
    the_numbers = []
    with open('18-1-input.txt') as f:
        in_line = f.readline().strip()
        while in_line:
            the_numbers.append(in_line)
            in_line = f.readline().strip()

    also_numbers = copy.deepcopy(the_numbers)
    max_answer = 0
    for idx, val in enumerate(the_numbers):
        val_eq = str_to_num(val)
        for also_idx, also_val in enumerate(also_numbers):
            also_eq = str_to_num(also_val)
            if idx != also_idx:
                list_answer = snail_add(val_eq, also_eq)
                mag_answer = calc_mag(list_answer)
                count += 1
                print(count, mag_answer)
                if mag_answer > max_answer:
                    max_answer = mag_answer
    print(max_answer)

if __name__ == '__main__':

    #PART ONE
    #process_input()

    #PART TWO
    #find_largest_magnitude()