# Advent of Code 2017
# Day 01 Inverse Captcha -- part 2

f = open('input.txt', 'r')
string = f.read()
# string = str(12131415)  # for test cases

digits = []

for n in range(len(string)):
    try:
        digits.append(int(string[n]))
    except ValueError:
        print('invalid value found')

sum = 0

length = len(digits)
half = int(length/2)

for m in range(length):
    if digits[m] == digits[(m + half) % length]:
        sum += digits[m]
        # print('match found at position {}, adding {}'.format(m, digits[m]))
        # print('Cummulative total = {} \n'.format(sum))
    else:
        pass

print('Final Total = {}'.format(sum))
