class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c=0
        
        res=0
        for i in range(len(nums)) :
            if nums[i] ==0:
                c+=1
                res+=c
                
            else:
                c=0
                
        return res