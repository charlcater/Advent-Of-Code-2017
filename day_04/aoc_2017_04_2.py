# Advent of Code 2017
# Day 04 High-Entropy Passphrases -- part 2
# correct answer = 231

lines = 0
invalid = 0

with open('input.txt', 'r') as f:

    for line in f.readlines():
        lines += 1

        # sort all strings alphabetically
        templist = []
        words = line.split()
        for phrase in words:
            b = sorted(phrase)
            sort_phrase = ''.join(b)
            # print(sortphrase)
            templist.append(sort_phrase)

            # then same as in part 1
            for phrase in templist:
                if templist.count(phrase) >= 2:
                    # print('duplicate phrase in line {}: {}'.format(lines, phrase))
                    invalid += 1
                    break
            else:
                continue
            break
        else:
            continue

valid = lines-invalid
print('Valid passphrases = {}'.format(valid))
