zzz = int(input())
ans = [-1]*zzz

locat = 0

for i in range(1,zzz+1):
    if i%2==0 and i%3==0 and i%5!=0:
        ans[locat] = i
        locat += 1

for j in range(0,zzz):
    if(ans[j+1]==-1):
        print(ans[j])
        break
    else:
        print(ans[j],end=", ")