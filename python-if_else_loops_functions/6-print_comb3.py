#!/usr/bin/python3
for i in range(1, 10):
    for j in range(1, 10):
        if i < j:
            if i == 8 and j == 9:
                print(89)
            else:
                print('{0}{1}'.format(str(i),str(j)), end=', ')
