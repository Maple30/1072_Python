def prime(pStart=2,pEnd=20):
    a = []
    for i in range(pStart,pEnd+1):
        for j in range(2,i+1):
            if(i%j == 0 and i != j):
                break;
            elif(i == j):
                a.append(i)
    for i in range(0,len(a)-1):
        print("{} ".format(a[i]),end='')
    print("{}".format(a[len(a)-1]))
    
M = int(input())
N = int(input())

prime(M,N)