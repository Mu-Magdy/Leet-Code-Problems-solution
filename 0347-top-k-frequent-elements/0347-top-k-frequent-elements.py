class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t={}
        
        for n in nums:
            if n in t:
                t[n]+=1
                
            else:
                t[n]=1
                
        t=dict(sorted(t.items(), key=lambda x: x[1], reverse=True))

        l=[x for x in t.keys()]
        print(l)
        return l[:k]
