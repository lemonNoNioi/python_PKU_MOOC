a = sorted(map(int, input().split()))
l = len(a)
b = {(a[i], a[j], a[k])
	for i in range(l)
	for j in range(i+1,l)
	for k in range(j+1,l)
	if a[i]+a[j]+a[k] == 0}
print(len(b))
