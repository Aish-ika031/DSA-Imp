class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        indegree = {i : 0 for i in range(1,n+1)}

        outdegree = {i : 0 for i in range(1 ,n+1)}

        for i in trust:

            indegree[i[1]] += 1

            outdegree[i[0]] += 1

        for i in range(1, n+1):

            if indegree[i] == n-1 and outdegree[i] == 0:

                return i

        return -1
        