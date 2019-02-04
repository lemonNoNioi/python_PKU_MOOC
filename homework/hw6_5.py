def bubbleSort(lst):
    for i in range(1,len(lst)):
        for j in range(len(lst)-i):
            if lst[j]>lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    
    return lst

alist=list(map(int,input().split()))
print(bubbleSort(alist))