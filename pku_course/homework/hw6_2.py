def hcf(n1, n2):
    a = n1
    while a%n2:
        a = a+ n1
    b = n1*n2//a
    return b

num1=int(input(""))
num2=int(input(""))
print(hcf(num1,num2))