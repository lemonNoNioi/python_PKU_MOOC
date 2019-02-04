import math
def is_sqr(n):
    a = int(math.sqrt(n))
    return a*a == n

i = 1
while 1:
    if is_sqr(i+150) and is_sqr(i+150+136):
        break
    i += 1
print(i)