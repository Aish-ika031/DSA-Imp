# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def bfs(root):
            
            q1=deque([])
            
            q1.append(root)
            
            res=[]
            
            level=0
            
            while len(q1)>0:
                
                curr=[]
                
                level=level+1
                
                n=len(q1)
                
                for _ in range(n):
                    
                    node=q1.popleft()
                    
                    curr.append(node.val)
                    
                    if node.left is not None:
                        
                        q1.append(node.left)
                        
                    if node.right is not None:
                        
                        q1.append(node.right)
                        
                if level%2:
                    
#                     curr=curr[::-1]
                    
#                     for i in curr:
                        
#                         res.append(i)
                      
                    st,end=0,len(q1)-1
        
                    while st<end:
                
                        q1[st].val,q1[end].val=q1[end].val,q1[st].val
                    
                        st=st+1
                        
                        end=end-1
                    
            return root
        
        return bfs(root)
                        
                    
