
import statistics
import math

def avg(lst):
    return sum(lst) / len(lst)

def align_crabs():

    with open('07-2-input.txt') as f:
        line = f.readline()
        fuel_cost = 0
        crab_positions = [int(x) for x in line.split(',')]
        med_pos = statistics.median(crab_positions)
        avg_pos = avg(crab_positions)
        avg_ceil = math.ceil(avg_pos)
        avg_flor = math.floor(avg_pos)
        for crab in crab_positions:
            n = abs(crab - avg_flor)
            fuel_cost += (n*(n+1))/2

        print(fuel_cost)




if __name__ == '__main__':
    align_crabs()