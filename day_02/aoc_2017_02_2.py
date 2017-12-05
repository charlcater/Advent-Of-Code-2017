# Advent of Code 2017
# Day 02 Corruption Checksum -- part 2

import csv

rowsum = []
checksum = 0

with open('input.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')

    for row in reader:
        rowlist = []
        for value in (row):
            rowlist.append(int(value))
        rowlist.sort(reverse=True)

        length = len(rowlist)  # 16

        i=0
        b = True

        for value in rowlist:
            for i in range(len(rowlist)):
                q = value / rowlist[i]
                if (q).is_integer() and q != 1.0:
                    checksum += q
                    # print(q)
                    # print('Cummalitave checksum = {}'.format(checksum))
                else:
                    pass

print('Valid inputs = {}'.format(valid))