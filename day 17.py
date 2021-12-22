
# THIS CODE COULD NOT BE MORE HIDEOUS, INEFFICIENT AND POORLY WRITTEN.
# I HAVE NO EXCUSE
# I INCLUDE SO THAT YOU MAY BEAR WITNESS TO MY SHAME



#target area: x=244..303, y=-91..-54

TARGET_AREA = [(244,303),(-91,-54)]
per_step_vel = {}
per_step_yvel = {}

def x_distance(in_x):
    return (in_x*(in_x+1))/2

#for a perfect hit
def get_x_velocity_range(in_target_x):
    min_xv = x_distance(in_target_x[0])
    max_xv = x_distance(in_target_x[1])
    return (min_xv,max_xv)

def get_y_velcoity_range(x_vel_range, in_target_y):
    pass

def calculate_velocity():
    pass

def add_to_psvel(steps, vel):
    global per_step_vel
    a_copy = []
    if steps in per_step_vel.keys():
        a_list = per_step_vel[steps]
        a_copy = a_list.copy()
        if vel not in a_copy:
            a_copy.append(vel)
    else:
        a_copy = [vel]

    per_step_vel[steps] = a_copy

def add_to_psyvel(steps, vel):
    global per_step_yvel
    a_copy = []
    if steps in per_step_yvel.keys():
        a_list = per_step_yvel[steps]
        a_copy = a_list.copy()
        if vel not in a_copy:
            a_copy.append(vel)
    else:
        a_copy = [vel]

    per_step_yvel[steps] = a_copy

def vel2pos_per_step(in_xvel, in_yvel, steps):
    xvel = in_xvel
    yvel = in_yvel
    xpos = 0
    ypos = 0
    for a_step in range(0,steps):
        xpos += xvel
        ypos += yvel
        xvel -= 1
        ypos -= 1
        if xvel < 0:
            xvel = 0

    return xvel, yvel


def calculate_x_range():

    x_vals = set()

    for idx in range(303,0,-1):
        count = 0
        curr_pos = idx
        curr_vel = idx
        steps = 1
        while (curr_vel >= 0):
            if (curr_pos >= 244) & (curr_pos <= 303):
                x_vals.add(idx)
                add_to_psvel(steps,idx)
                if curr_vel == 0:
                    for pad_zeros in range(1,300):
                        add_to_psvel(steps+pad_zeros, idx)

            curr_vel -= 1
            curr_pos += curr_vel
            steps += 1


    for idx in range(-91,93):
        count = 0
        curr_pos = idx
        curr_vel = idx
        steps = 1
        while (curr_pos >= -91):
            if (curr_pos >= -91) & (curr_pos <= -54):
                x_vals.add(idx)
                add_to_psyvel(steps, idx)

            curr_vel -= 1
            curr_pos += curr_vel
            steps += 1

    print(per_step_vel)
    print(per_step_yvel)

    # for elem, val in per_step_vel.items():
    #     print(elem, val)

    count = 0
    counted = set()
    for elem, val in per_step_vel.items():
        if elem in per_step_yvel.keys():
            yval = per_step_yvel[elem]
            print(elem, len(val), len(yval))
            for anx in val:
                for any in yval:
                    if (anx,any) not in counted:
                        count +=1
                        counted.add((anx,any))

            #count += len(val) * len(per_step_yvel[elem])

    print(count, len(counted))


if __name__ == '__main__':
    calculate_x_range()