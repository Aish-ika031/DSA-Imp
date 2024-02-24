# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head == None or k == 0 or head.next == None :
            return head

        l = 1

        s1 = head

        while s1.next:

            l=l+1

            s1=s1.next

        s1.next = head

        k = k%l

        end = l - k 

        while end:

            s1 = s1.next

            end = end - 1

        head = s1.next

        s1.next = None

        return head

        
        