pwd = input()

zz = u""
zz = pwd

if (not pwd.isupper()) and (not pwd.islower()) and ( not pwd.isdecimal()) and len(pwd) >= 6 and len(pwd) <= 12:
    print("密碼設定完成")
else:
    print("密碼不符合規定")
