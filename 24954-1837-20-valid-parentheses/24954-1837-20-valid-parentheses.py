class Solution:
    def isValid(self, s: str) -> bool:
        d={'}':'{',
            ')':'(',
            ']':'['}
        st=[]
        for i in s:
            if i not in d:
                st.append(i)
                continue
            elif not st or st[-1]!=d[i]:
                return False
            st.pop()

        return not st