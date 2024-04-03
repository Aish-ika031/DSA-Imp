class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        arr_i=[0,-1,0,1]
        arr_j=[-1,0,1,0]
        def dfs(board,i,j,l,word):
            if l>=len(word):
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False
            if board[i][j]!=word[l]:
                return False
            
            curr=board[i][j]
            board[i][j]='#'
            val=dfs(board,i+1,j,l+1,word) or dfs(board,i-1,j,l+1,word) or dfs(board,i,j+1,l+1,word) or dfs(board,i,j-1,l+1,word)
            board[i][j]=curr
            return val
        k=0
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j]==word[0]:
                    if dfs(board,i,j,0,word):
                        return True
        return False
    
            