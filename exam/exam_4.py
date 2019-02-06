alist = list(map(int,input().split()))
blist = []
for i in range(len(alist)):
    s = 1
    for j in range(len(alist)):
        if i == j:
            continue
        s *= alist[j]
    blist.append(s)
print(blist)
