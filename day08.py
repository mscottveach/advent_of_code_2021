
code = {'a': '', 'b': '', 'c': '', 'd':'', 'e':'', 'f':'', 'g':''}
digits = {'abcefg':0, 'cf':1, 'acdeg':2, 'acdfg':3, 'bcdf':4, 'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9}
search_digits = [1,4,7,8]

# ALGORITHM:
# c, f = the two lenght
# a = three length - c    *
# b, d = four length - c
# g = 6 length - (a + c + b)  *
# d = 5 length with (a, c, g and only of b) *
# b = what d is not *
# f = 5 length with (a, b, d, g and only of c/f) *
# c = what f is not *
# e = 6 length - (a, b, c, f, g)*

def solve_wiring(in_wiring, the_output):
    global code
    #print(in_wiring)
    #print(code)
    for segments in in_wiring:
        if len(segments) == 2:
            code['c'] = segments

    for segments in in_wiring:
        if len(segments) == 3:
            code['a'] = remove_letters(segments,code['c'])

    for segments in in_wiring:
        if len(segments) == 4:
            code['b'] = remove_letters(segments,code['c'])

    #print(code)

    for segments in in_wiring:
        if len(segments) == 6:
            compare_string = code['a'] + code['b'] + code['c']
            if chars_in_string(segments, compare_string):
                code['g'] = remove_letters(segments,compare_string)


    #print(code)

    for segments in in_wiring:
        if len(segments) == 5:
            compare_string = code['a'] + code['c'] + code['g']
            if chars_in_string(segments, compare_string):
                code['d'] = remove_letters(segments, compare_string)

    #print(code)

    code['b'] = remove_letters(code['b'],code['d'])

    for segments in in_wiring:
        if len(segments) == 5:
            compare_string = code['a'] + code['b'] + code['d'] + code['g']
            if chars_in_string(segments, compare_string):
                code['f'] = remove_letters(segments, compare_string)

    #print(code)

    code['c'] = remove_letters(code['c'], code['f'])

    #print(code)

    for segments in in_wiring:
        if len(segments) == 7:
            compare_string = code['a'] + code['b'] + code['c'] + code['d'] + code['f'] + code['g']
            if chars_in_string(segments, compare_string):
                #print(segments, compare_string)
                code['e'] = remove_letters(segments, compare_string)

    #print(code)
    #print('****')
    #print(the_output)
    local_digit_cnt = 0
    str_digit = ''
    for digit in the_output:
        correct_digit = convert_digit(digit)
        str_digit += str(correct_digit)
        #print(digit,correct_digit)
        if correct_digit in search_digits:
            local_digit_cnt += 1

    #return(local_digit_cnt)
    return(int(str_digit))

def get_key(val):
    global code
    for key, value in code.items():
        if val == value:
            return key

def convert_digit(in_digit):
    new_string = ''
    #print(in_digit)
    for char in in_digit:
        new_string += get_key(char)
    sorted_list = sorted(new_string)
    #print(sorted_list)
    return digits["".join(sorted_list)]


def chars_in_string(in_string, in_letters):
    ret_value = True
    for char in in_letters:
        if char not in in_string:
            ret_value = False
    return(ret_value)

def remove_letters(in_string, in_letters):
    for char in in_letters:
        in_string = in_string.replace(char,'')
    return(in_string)

def grab_data():
    with open('08-1-input.txt') as f:
        line = f.readline()
        wires = []
        output = []
        while line:
            wires.append(((line.split('|'))[0].strip()).split(' '))
            output.append(((line.split('|'))[1].strip()).split(' '))
            line = f.readline()

    return(wires, output)



if __name__ == '__main__':

    the_wiring, the_output = grab_data()
    global_digit_count = 0
    for idx, a_wire in enumerate(the_wiring):
        global_digit_count += solve_wiring(a_wire, the_output[idx])

    print(global_digit_count)


# dgabec cfgeb cfb cefd cdabfg gbdce fc begdfc gfbea febacdg | bcfdaeg cf fc gecabdf