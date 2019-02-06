alist = list(map(int,input().split()))
l = len(alist)
result = []
for i in range(l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            if alist[i]+alist[j]+alist[k] == 0:
                rlist = sorted([alist[i],alist[j],alist[k]])
                result.append(rlist)

result = list(set([tuple(t) for t in result]))
print(len(result))
