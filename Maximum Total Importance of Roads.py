class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        graph = [0] * n

        for i in roads:

            graph[i[0]] += 1

            graph[i[1]] += 1

        graph.sort()

        cnt = 1

        curr = 0

        for i in graph:

            curr += cnt * i

            cnt += 1

        return curr