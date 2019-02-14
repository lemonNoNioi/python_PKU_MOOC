a = map(int, input().split())
b = map(int, input().split())
c = sum(map(lambda x,y:(x-y)**2, a, b))
print(c)
