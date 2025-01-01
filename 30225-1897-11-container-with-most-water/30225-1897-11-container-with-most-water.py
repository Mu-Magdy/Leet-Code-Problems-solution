class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        res=0

        while l<r:
            cur_res=min(heights[l],heights[r])*(r-l)
            res=max(res,cur_res)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            
        return res
            
        