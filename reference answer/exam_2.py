a = input()
b = ''.join(map(lambda x:x.lower() if x.isdigit() or x.isalpha() else '', a))
print(b==b[::1])
