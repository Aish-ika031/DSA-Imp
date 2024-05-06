# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(root):

            prev , curr = None , root

            while curr:

                nxt = curr.next

                curr.next , prev , curr = prev , curr , nxt

            return prev

        node = ListNode()

        node.next = reverse(head)

        mx = 0

        prev , curr = node , node.next

        while curr:

            mx = max(mx , curr.val)

            if curr.val < mx:

                prev.next = curr.next

            else:

                prev = prev.next

            curr = curr.next

        return reverse(node.next)