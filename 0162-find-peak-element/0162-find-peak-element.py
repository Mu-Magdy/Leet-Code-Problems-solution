class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,h=0,len(nums)-1
        while l<h:
            middle=(h+l)//2
            if nums[middle]<nums[middle+1]:
                l=middle+1
            else:
                h=middle
            
        return l
          
            
  