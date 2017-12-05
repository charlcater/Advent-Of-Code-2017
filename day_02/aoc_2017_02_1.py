# Advent of Code 2017
# Day 02 Corruption Checksum -- part 1

import csv

rowsum = []
checksum = 0

with open('input.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        rowlist = []
        for value in (row):
            rowlist.append(int(value))

        diff = max(rowlist) - min(rowlist)
        checksum += diff

print('Checksum = {}'.format(checksum))