class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s =set(nums)
        
        longest=0
        for i in nums:
            long=0

            if i-1 not in s:
                while long+i in s:
                    long+=1
                
                longest=max(longest,long)
            
        return longest
    