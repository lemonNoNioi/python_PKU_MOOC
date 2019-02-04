lst = list(map(int,input().split()))
s = int(input())
def select(lst, s):
    for a in lst:
        for b in lst:
            if a!=b  and a+b == s:
                return sorted([lst.index(a), lst.index(b)])
print(select(lst, s))