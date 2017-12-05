# Advent of Code 2017
# Day 04 High-Entropy Passphrases -- part 1
# correct answer = 337

# ## count invalid phrases, no csv
# lines = 0
# invalid = 0

# with open('input.txt', 'r') as f:

#     for line in f.readlines():
#         lines += 1

#         words = line.split()
#         for phrase in words:
#             if words.count(phrase) >= 2:
#                 # print('duplicate phrase: {phrase}'.format(phrase=phrase))
#                 invalid += 1
#                 break
#             else:
#                 continue

# valid = lines-invalid
# print('Valid passphrases = {}'.format(valid))


#  count valid phrases, with csv
import csv
valid = 0

with open('input.txt', 'r') as f:
    reader = csv.reader(f, delimiter=' ')

    for line in reader:
        setOne = set(line)

        if len(setOne.intersection(setOne)) == len(line):
            # print('valid passphrase found')
            valid += 1
        else:
            continue
        
print('Valid passphrases = {}'.format(valid))