"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root==None:
            return []
        s1=[]
        res=[]
        s1.append(root)
        while len(s1)>0:
            curr=s1.pop()
            res.append(curr.val)
            for i in curr.children:
                s1.append(i)
        return res[::-1]
            
        