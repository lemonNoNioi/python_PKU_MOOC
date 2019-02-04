s = str(input())
n = int(input())
l = len(s)
while n > l:
    n = n - l
print(s[n:]+s[:n])