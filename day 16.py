import math

VER_STACK = []
store_literals = []
eq_stack = []

hex_bin_dict = {'0': '0000',
              '1': '0001',
              '2': '0010',
              '3': '0011',
              '4': '0100',
              '5': '0101',
              '6': '0110',
              '7': '0111',
              '8': '1000',
              '9': '1001',
              'A': '1010',
              'B': '1011',
              'C': '1100',
              'D': '1101',
              'E': '1110',
              'F': '1111' }


def get_literal(in_literal):
    count = 0
    the_number = ''

    while in_literal[count] != '0':
        the_number += in_literal[count+1:count+5]
        count += 5
    else:
        the_number += in_literal[count+1:count+5]

    count += 5

    if count == len(in_literal):
        out_literal = ''
    else:
        out_literal = in_literal[count:]

    return the_number, out_literal


def process_operator_packet(in_packet):

    local_cursor = 0
    length_type_id = in_packet[local_cursor]
    local_cursor += 1
    if length_type_id == '0':
        subpack_length = int(in_packet[local_cursor:local_cursor+15],2)
        local_cursor += 15
        sub_pack = in_packet[local_cursor:local_cursor+subpack_length]
        rest_of_packet = unpack_packet(sub_pack)
        while rest_of_packet:
            rest_of_packet = unpack_packet(rest_of_packet)

        local_cursor = local_cursor + subpack_length
        if local_cursor == len(in_packet):
            rest_of_packet = ''
        else:
            rest_of_packet = in_packet[local_cursor:]
    else:
        num_of_subpacks = int(in_packet[local_cursor:local_cursor+11],2)
        local_cursor += 11

        rest_of_packet = in_packet[local_cursor:]
        for idx in range(0,num_of_subpacks):
            rest_of_packet = unpack_packet(rest_of_packet)

    return rest_of_packet


def unpack_packet(in_packet):
    global eq_stack
    cursor = 0

    global VER_STACK
    global store_literals
    ver = in_packet[0:3]
    id = in_packet[3:6]
    cursor += 6
    VER_STACK.append(ver)

    if id == '100':
        the_literal, out_packet = get_literal(in_packet[cursor:])
        eq_stack.append(int(the_literal,2))
    else:
        eq_stack.append(id)
        eq_stack.append('(')
        out_packet = process_operator_packet(in_packet[cursor:])
        eq_stack.append(')')

    return out_packet

def hex_to_bin(in_packet):
    out_packet = ''
    for char in in_packet:
        out_packet += hex_bin_dict[char]

    return out_packet

def process_eq_stack(in_stack):

    hold_nums = []

    while len(hold_nums) != 1:
        act_nums = []

        elem = in_stack.pop()
        while elem != '(':
            hold_nums.append(elem)
            elem = in_stack.pop()

        elem = hold_nums.pop()
        while elem != ')':
            act_nums.append(elem)
            elem = hold_nums.pop()

        elem = in_stack.pop()

        if elem == '000':
            res = sum(act_nums)
        elif elem == '001':
            res = math.prod(act_nums)
        elif elem == '010':
            res = min(act_nums)
        elif elem == '011':
            res = max(act_nums)
        elif elem == '101':
            if act_nums[0] > act_nums[1]:
                res = 1
            else:
                res = 0
        elif elem == '110':
            if act_nums[0] < act_nums[1]:
                res = 1
            else:
                res = 0
        elif elem == '111':
            if act_nums[0] == act_nums[1]:
                res = 1
            else:
                res = 0

        hold_nums.append(res)

    print(hold_nums.pop())

if __name__ == '__main__':
    #test_literal = '110100101111111000101000'
    #test_literal = '00111000000000000110111101000101001010010001001000000000'
    #test_literal = 'EE00D40C823060'
    #test_literal = '8A004A801A8002F478'
    #test_literal = '620080001611562C8802118E34'
    #test_literal = 'C0015000016115A2E0802F182340'
    #test_literal = 'A0016C880162017C3686B18A3D4780'

    #test_literal = 'C200B40A82'
    #test_literal = '04005AC33890'
    #test_literal = '880086C3E88112'

    #test_literal = 'CE00C43D881120'
    #test_literal = 'D8005AC2A8F0'
    #test_literal = 'F600BC2D8F'
    #test_literal = '9C005AC2F8F0'
    #test_literal = '9C0141080250320F1802104A08'


    with open('16-1-input.txt') as f:
        hex = f.readline()
    #hex = test_literal
    rop = hex_to_bin(hex)
    rop = unpack_packet(rop)

    print(''.join(str(c) for c in eq_stack))
#    eq_stack = eq_stack.reverse()
    process_eq_stack(eq_stack)

    # ver_count = 0
    # for elem in VER_STACK:
    #     ver_count += int(elem,2)
    # print(ver_count)