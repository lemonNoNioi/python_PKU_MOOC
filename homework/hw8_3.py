import math

class Sloution:
    def powerfulInt(self, x, y, n):
        i = 1 if x == 1 else int(math.log(n, x))+1
        j = 1 if y == 1 else int(math.log(n, y))+1
        res = set()
        for a in range(i):
            for b in range(j):
                tmp = x**a+y**b
                if tmp<=n:
                    res.add(tmp)
        return sorted(list(res))


x = int(input())
y = int(input())
n = int(input())
print(Sloution().powerfulInt(x,y,n))
