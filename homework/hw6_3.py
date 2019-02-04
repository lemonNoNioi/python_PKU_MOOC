def lcm(n1, n2):
    a = n1
    while a%n2:
        a = a+ n1
    return a

num1=int(input(""))
num2=int(input(""))
print(lcm(num1,num2))