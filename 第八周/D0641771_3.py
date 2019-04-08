chose = 1
myDic = {'dog':'狗','cat':'貓'}
while(1):
    chose = int(input("(1): 英翻中\n"+"(2) 中翻英"+"\n(3) 離開:\n"))
    if chose == 3:
        break
    elif chose == 2:
        translate = input("請輸入中文單字:")
        if translate in myDic.values():
            print(list (myDic.keys()) [list (myDic.values()).index (translate)])
        else:
            print("抱歉 字典沒有這個字")
    elif chose == 1:
        translate = input("請輸入英文單字:")
        if translate in list(myDic.keys()):
            print(myDic[translate])
        else:
            print("抱歉 字典沒有這個字")

