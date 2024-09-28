class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n=0
        for char in columnTitle:
            n=n*26+(ord(char)-64)
            print(n)
        return n