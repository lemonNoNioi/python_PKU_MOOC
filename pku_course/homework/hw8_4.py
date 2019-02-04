class Solution:
    def maxTriC(self, lst):
        lst = sorted(lst,reverse=True)
        for i in range(2,len(lst)):
            if lst[i] + lst[i-1] > lst[i-2]:
                return lst[i]+lst[i-1]+lst[i-2]
        return 0

lst = list(map(int, input().split()))
print(Solution().maxTriC(lst))