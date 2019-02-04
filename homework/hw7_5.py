def josephus(n,k):
    link = list(range(n)) 
    ind = 0
    lst = []
    for i in range(n):
        ind = (ind+k) % len(link) 
        ind -= 1
        lst.append(link.pop(ind))
        if ind == -1: # the last element of link
            ind=0
    return lst

a = int(input())
b = int(input())
print(josephus(a, b))