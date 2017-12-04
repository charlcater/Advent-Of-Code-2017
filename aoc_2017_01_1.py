# Advent of Code 2017
# Day 01 excercise 1

f = open('input.txt', 'r')
string = f.read()
# string = str(91212129)  # for test cases

digits = []

for n in range(len(string)-1):
    if type(string[n]) == str:
        digits.append(int(string[n]))
    else:
        pass

digits.append(int(string[0]))  # prettify!

# print(digits)

sum = 0

for m in range(len(digits) - 1):
    if digits[m] == digits[m + 1]:
        sum += digits[m]
        print('match found at position {}, adding {}'.format(m, digits[m]))
        print('Cummulative total = {} \n'.format(sum))
    else:
        pass

print('Final Total = {}'.format(sum))
