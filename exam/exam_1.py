alist = input().split()
blist = input().split()
c = 0
for i in range(len(alist)):
    c += (int(alist[i])-int(blist[i]))**2
print(c)
