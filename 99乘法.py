arry = [-1]*10
for i in range(1,10):
    for j in range(1,10):
        arry[j-1] = i*j
    print("{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d} {7:2d} {8:2d}".format(arry[0],arry[1],arry[2],arry[3],arry[4],arry[5],arry[6],arry[7],arry[8]))