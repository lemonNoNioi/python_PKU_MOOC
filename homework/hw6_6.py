def foo(lst):
    blist = []
    for i in range(len(lst)):
        if i%2:
            blist.append(lst[i])
    return blist

alist=list(map(int,input().split()))
print(foo(alist))