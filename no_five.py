m = int(input())
n = int(input())

gcdm = m
gcdn = n
gcdr = 0
while gcdn!=0:
    gcdr = gcdm%gcdn
    print("gcdr=",gcdr)
    gcdm = gcdn
    print("gcdm=",gcdm)
    gcdn = gcdr
    print("gcdn=",gcdn)

print("gcd =",gcdm,"; lcm =",m*n//gcdm)
