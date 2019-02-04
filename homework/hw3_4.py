s = str(input())
c = s[-1]
i = 0
for j in range(len(s)):
    if s[j] == c:
        i += 1
print(i-1)