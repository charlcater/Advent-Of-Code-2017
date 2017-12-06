# Advent of Code 2017
# Day 05: A Maze of Twisty Trampolines, All Alike -- part 1

with open('input.txt', 'r') as f:

    lst = [int(i) for i in f.read().splitlines()]
    # lst = [0, 3, 0, 1, -3]

    try:
        position = 0
        step = 0

        while True:
            old_pos = position
            jump_to = lst[position]
            position += jump_to
            step += 1

            if jump_to >= 3:
                lst[old_pos] += -1
            else:
                lst[old_pos] += 1

    except IndexError:
        print('Out of bounds: steps taken: {}'.format(step))
        # print(lst)
