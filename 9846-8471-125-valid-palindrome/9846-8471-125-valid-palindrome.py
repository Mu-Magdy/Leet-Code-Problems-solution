class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                t+=s[i].lower()
        
        print(t)
        l , r=0,len(t)-1
        
        while l<=r:
            
            if t[l]!=t[r]:
                return False
            l+=1
            r-=1

        return True