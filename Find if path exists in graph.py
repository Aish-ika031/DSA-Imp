class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        g = [[] for _ in range(n)]
        
        for s,e in edges:
            g[s].append(e)
            g[e].append(s)
            
        visited = [False] * n
        
        self.dfs(g, visited, start)
        
        return visited[end]
    
    def dfs(self, g, visited, v):
        visited[v] = True
        
        for to in g[v]:
            if not visited[to]:
                self.dfs(g, visited, to)