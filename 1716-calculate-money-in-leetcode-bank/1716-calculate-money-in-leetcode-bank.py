class Solution:
    def totalMoney(self, n: int) -> int:
        weeks=n//7
        low=28
        high=28+(7*(weeks-1))
        res=weeks*(low+high)//2
        
        for i in range(n%7):
            res+=i+ weeks+1
            
        return res