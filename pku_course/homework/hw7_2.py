import math
x = int(input())
result = math.sin(15/180*math.pi) + (math.exp(x)-5*x)/(math.sqrt(x*x+1)) - math.log(3*x,math.e)
print(round(result,10))