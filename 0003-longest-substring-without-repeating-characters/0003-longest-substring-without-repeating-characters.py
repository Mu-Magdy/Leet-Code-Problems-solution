class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        u=set()
        l=0
        for r in range(len(s)):
            while s[r] in u:
                u.remove(s[l])
                l+=1
                
            u.add(s[r])
            res=max(res,r-l+1)
            
        return res
                