# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes=[]

        res=ListNode(0)

        for i in lists:

            while i!=None:

                nodes.append(i.val)

                i=i.next

        curr=res

        nodes=sorted(nodes)

        for i in nodes:

            res.next=ListNode(i)

            res=res.next

        return curr.next
