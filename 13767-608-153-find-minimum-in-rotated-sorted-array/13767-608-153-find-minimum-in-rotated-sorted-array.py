class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=10000
        while l<=r:
            m=(l+r)//2
            if nums[r]<nums[m]:
                l=m+1
                res=min(nums[m],res)
            else:
                r=m-1
                res=min(nums[m],res)

        return res
            
