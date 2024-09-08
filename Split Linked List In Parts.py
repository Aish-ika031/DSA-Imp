# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        def length(head):

            cnt = 0

            while head:

                cnt += 1

                head = head.next

            return cnt

        i = 0

        l = length(head)

        each_size = l // k

        extra = l % k

        res = [None] * k

        curr , prev = head , None

        while i < k:

            res[i] = curr

            print(res)

            for j in range(0 , each_size + (extra > 0) - 1):

                if curr:

                    curr = curr.next

            if curr:

                print(0)

                prev = curr.next

                curr.next = None

                curr = prev
            
            print(curr)

            i += 1

            extra -= 1

        return res