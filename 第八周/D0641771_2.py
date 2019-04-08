stu_set = {'S' + str(x) for x in range(1,51)}
game_set = {'S' + str(i) for i in random.sample(range(1,51),10)}
gta_set = {'S' + str(j) for j in random.sample(range(1,51),10)}

print('都參加的:'+str(game_set&gta_set))
print('參加吉他社沒有參加電腦社:'+str(gta_set-game_set))
print('參加電腦社沒有參加吉他社:'+str(game_set-gta_set))
print('都沒有參加:'+str(stu_set-(game_set|gta_set)))