class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        indegree = [0 for _ in range(n)]
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
            indegree[s]+=1
            indegree[e]+=1
        queue = deque([])
        for i in range(len(indegree)):
            if indegree[i]==1:
                queue.append(i)
        ans = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                indegree[node] = 0
                if values[node]%k==0:
                    ans+=1
                    for neighbor in graph[node]:
                        indegree[neighbor]-=1
                        if indegree[neighbor]==1:
                            queue.append(neighbor)
                else:
                    for neighbor in graph[node]:
                        indegree[neighbor]-=1
                        values[neighbor]+=values[node]
                        if indegree[neighbor]==1:
                            queue.append(neighbor)
        if ans==0:
            return 1
        return ans
