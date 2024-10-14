class Solution:
    def addBinary(self, a: str, b: str) -> str:
#         a_len=len(a)
#         b_len=len(b)
#         x=0
#         y=0
#         for i in range(a_len):
#             if a[i]=="1":
#                 x+=2**(a_len-i)
        
#         for i in range(b_len):
#             if b[i]=="1":
#                 y+=2**(b_len-i)
                
#         s=x+y
#         c=''
#         while s>0:
#             if s
            
        x=int(a,2)
        y=int(b,2)
        return format(x+y,'b')
            
            