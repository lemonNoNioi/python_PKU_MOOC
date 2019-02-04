import time
t = input()
structTime = time.strptime(t,'%Y/%m/%d')
print(structTime[7])