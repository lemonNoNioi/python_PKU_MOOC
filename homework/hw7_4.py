n = int(input())
for i in range(1,2*n):
    for j in range(1,2*n):
        if i == j or i+j == 2*n:
            print('X',end='')
        else:
            print('+',end='')
    print('\n',end='')