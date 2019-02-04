class Student:
    def __init__(self, sname, mscore, cscore, escore):
        self.sname = sname
        self.mscore = mscore
        self.cscore = cscore
        self.escore = escore
        self.sumscore = mscore+cscore+escore
    def __lt__(self, other):
        return self.sumscore < other.sumscore
    def __str__(self):
        return "%s %d %d %d" % (self.sname, self.mscore, self.cscore, self.escore)
    __repr__ = __str__

sname = input().split()
mscore = list(map(int, input().split()))
cscore = list(map(int, input().split()))
escore = list(map(int, input().split()))
l = []
for i in range(len(sname)):
    s = Student(sname[i],mscore[i],cscore[i],escore[i])
    l.append(s)
l.sort()
print(l[-1])
