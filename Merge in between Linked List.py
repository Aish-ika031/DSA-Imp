# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        st = ListNode()

        bk = list1

        for i in range(b):

            if i == a-1:

                st = bk

            bk = bk.next

            # if i == a-1:

            #     st = bk

        st.next = list2

        while list2.next:

            list2 = list2.next

        list2.next = bk.next

        # bk.next = None

        return list1

