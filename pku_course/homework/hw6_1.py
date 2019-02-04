def fbnq(i):
    lst = [1,1]
    for ii in range(2,i):
        lst.append(lst[ii-2]+lst[ii-1])
    return lst[i-1]

n = int(input(""))
print(fbnq(n))