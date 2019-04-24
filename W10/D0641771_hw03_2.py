def poll(org=False, *cdd):
    Name = ['柯文哲','丁守中','姚文智']

    f = open('poll.csv', 'r')
    a = f.readlines()
    a.pop(0)
    # print(a)
    f = open('poll.csv', 'r')
    Data ={}
    for j in a:
        Data[j.split(",")[0]] = {'TV':j.split(",")[0],'柯文哲':j.split(",")[2],'丁守中':j.split(",")[3],'姚文智':j.split(",")[4]}
    check = f.read()
    for i in org:
        if(check.find(i)==-1):
            print("您輸入了不存在的媒體\n")
            return 0
    cdd = list(cdd)

    if org==False:
        print("請輸入媒體名稱\n")
        return 0
    if len(cdd) > 3:
        print("輸入人數超過候選人人數\n")
    elif len(cdd)==0:
        print("\t柯\t丁\t姚")
        for k in org:
            print("{}\t{}\t{}\t{}".format(Data[k]['TV'],Data[k]['柯文哲'],Data[k]['丁守中'],Data[k]['姚文智']),end='')
    else:
        for l in cdd:
            if l not in Name:
                print("不存在的候選人\n")
                return 0
        Buff_Name = []
        for M in Name:
            if M in cdd:
                print("\t{}".format(M[0]),end='')
                Buff_Name.append(M)
        print("\n")
        for N in org:
            print("{}\t{}\t{}".format(Data[N]['TV'],Data[N][Buff_Name[0]],Data[N][Buff_Name[1]],end=''))
    print("\n")

m = ('TVBS','Yahoo')
poll(m)
