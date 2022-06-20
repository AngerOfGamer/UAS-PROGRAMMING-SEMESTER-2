r = 5
f = 2 * r - 2
for t in range(0, r):
    for g in range(0, f):
        print(' ', end='')
    f -= 2
    for g in range(0, t + 1):
        print(' *', end='')
    print('')