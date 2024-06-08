class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count={}
        for w,h in rectangles:
            if w/h in count:
                count[w/h]+=1
            else:
                count[w/h]=1
        res=0
        for c in count.values():
            if c>1:
                res+=(c*(c-1))//2
                
        return res
      