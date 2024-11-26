class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        degree = [0] * n

        for i in edges:

            degree[i[1]] += 1

        cnt = 0

        player = -1

        for i in range(n):

            if degree[i] == 0:

                cnt += 1

                player = i

        if cnt == 1:

            return player 

        else:
            
            return -1
