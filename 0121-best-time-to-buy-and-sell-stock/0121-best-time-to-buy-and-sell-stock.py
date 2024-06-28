class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        curr=10000
        for i in prices:
            if curr>i:
                curr=i
            else:
                profit=max(profit,i-curr)
                
        return profit