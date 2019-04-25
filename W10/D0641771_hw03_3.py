name = ['Selena Gomez','Cristiano Ronaldo','Ariana Grande', 'Kim Kardashian', 'Beyoncé Giselle Knowles', 'Taylor Swift', 'Kylie Jenner', 'Dwayne Johnson', 'Justin Bieber', 'Neymar da Silva Santos Júnior']

for i,st in enumerate(name):
    name[i] = tuple(st.split())
name = sorted(name, key=lambda x : x[-1])
for i in name:
    for j in i:
        print("{} ".format(j),end='')
    print("\n")