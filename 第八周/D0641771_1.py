monster_list = ['地精','狼人','熊貓人']

attack_list = [80,90,20]
defense_list = [70,92,75]
monster = {}
for i in range(0,3):
    monster[monster_list[i]] = (attack_list[i],defense_list[i])
print(monster)