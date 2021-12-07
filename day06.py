
ancestors_in_days = {}
STARTING_DAYS = 256

def spawn_by_day():
    spawners_on_day = {}
    for idx in range(0, 9):
        spawners_on_day[idx] = 0

    with open('06-1-input.txt') as f:
        line = f.readline()
        ints = [int(x) for x in line.split(',')]
    for a_num in ints:
        spawners_on_day[a_num] += 1

    total_days = 0
    day_spawners = 0
    print(spawners_on_day)
    children_to_be_born = 0
    for current_day in range(0,STARTING_DAYS+1):
        day8s = spawners_on_day[8]
        day7s = spawners_on_day[7]
        spawners_on_day[7] = day8s
        spawners_on_day[8] = children_to_be_born
        who_had_babies_yesterday = (current_day - 1) % 7
        spawners_on_day[who_had_babies_yesterday] += day7s
        who_spawns = current_day % 7
        children_to_be_born = spawners_on_day[who_spawns]

        print(who_spawns, children_to_be_born)

    total_count = 0
    for idx in range(0,9):
        total_count += spawners_on_day[idx]
    print(spawners_on_day)
    print(total_count, children_to_be_born)


if __name__ == '__main__':
    spawn_by_day()