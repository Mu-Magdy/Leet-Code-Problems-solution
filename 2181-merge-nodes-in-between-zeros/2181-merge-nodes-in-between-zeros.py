# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=head.next
        r=l
        
        while r:
            total=0
            while r.val!=0: 
                total+=r.val
                r=r.next
                
            l.val=total
            
            r=r.next
            l.next=r
            l=l.next
            
        return head.next
            
            