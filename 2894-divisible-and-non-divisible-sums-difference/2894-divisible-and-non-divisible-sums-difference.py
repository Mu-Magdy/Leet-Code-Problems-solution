class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res=0
        dev=0
        for i in range(n+1):
            if i%m==0:
                dev+=i
            else:
                res+=i
        return res-dev