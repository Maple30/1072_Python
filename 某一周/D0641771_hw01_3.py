Fib = [0]*20
Fib[1] = 1

print("0 1 ",end="")
for i in range(2,100):
    if Fib[i-2]+Fib[i-1] > 100:
        break
    else:
        Fib[i] = Fib[i-2]+Fib[i-1]
        print(Fib[i],end=" ")