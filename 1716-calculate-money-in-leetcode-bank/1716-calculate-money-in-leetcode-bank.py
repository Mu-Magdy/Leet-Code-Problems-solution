class Solution:
    def totalMoney(self, n: int) -> int:
        res=0
        day=0
        dep=1
        
        while day<n:
            res+=dep
            day+=1
            dep+=1
            
            if day%7==0:
                dep=1+day//7
                
        return res