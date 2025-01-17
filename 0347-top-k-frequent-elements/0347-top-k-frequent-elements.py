class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)] 
        
        for n in nums:
            count[n]=1+count.get(n,0)
            
        for n,c in count.items():
            freq[c].append(n)
            
        l=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                l.append(j)
                if len(l)==k:
                    return l
                    
