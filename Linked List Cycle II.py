# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s1=head
        s2=set()
        while s1:
            if s1 in s2:
                return s1
            s2.add(s1)
            s1=s1.next
        return None