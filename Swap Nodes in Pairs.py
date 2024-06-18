# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def r(head):

            if head==None or head.next==None:

                return head

            s1=head.next

            head.next=r(s1.next)

            s1.next=head

            return s1
            
        return r(head)