# Advent of Code 2017
# Day 06: Memory Reallocation -- part 1 & 2

with open('input.txt', 'r') as f:

    # lst = [0, 2, 7, 0]  # test input
    lst = [int(i) for i in f.read().split()]
    length = len(lst)
    lstoflsts = []
    testset = {}

    rounds = 0
    newlst = list(lst)

    while len(testset) == len(lstoflsts):
        looplst = list(newlst)
        lstoflsts.append(looplst)

        newlist = list(looplst)
        m = max(newlst)
        maxpos = newlst.index(m)
        # print('max = {}, maxpos = {}'.format(m, maxpos))

        newlst[maxpos] = 0
        for i in range(m):
            updatepos = maxpos + i + 1
            newlst[updatepos % length] += 1

        testset = set(tuple(x) for x in lstoflsts)
        looplst = list(newlst)
        rounds += 1

    else:
        if len(testset) < len(lstoflsts):
            print('Duplicate found in round {}'.format(rounds - 1))

    # find the duplicate, get index and loop length
    j = 0
    k = 0
    for j in range(len(lstoflsts)):
        for k in range(len(lstoflsts)):
            if lstoflsts[j] == lstoflsts[k] and not j == k:
                # print(j, k)
                # print(lstoflsts[j], lstoflsts[k])
                print('Loop length = {} rounds'.format(abs(j - k)))
                break
        else:
            continue
        break
