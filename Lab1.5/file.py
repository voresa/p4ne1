import glob
li = glob.glob('C:\\tmp\\config_files\\*.*')
print(li)
spisok=[]
for i in li:
    with open(i) as file:
        for s in file:
           if 'ip address ' in s:
#               spisok.append(list(set(s)))
                print(s)
                spisok.append(set(s))

#           spisok.append(set(list(s)))

print(spisok)
#l = sorted(list(set(list(open(’test.csv')))))
