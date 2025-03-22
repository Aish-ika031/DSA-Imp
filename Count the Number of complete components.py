class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        def bfs(graph , node):

            q1 = deque()

            q1.append(node)

            res = []

            vis[node] = True

            while len(q1) > 0:

                cur_node = q1.popleft()

                res.append(cur_node)

                for i in graph[cur_node]:

                    if vis[i] == False:

                        vis[i] = True

                        q1.append(i)

            return res

        def check(res):

            status = False

            for i in res:

                if len(graph[i]) != len(res) - 1:

                    return False

            return True

        graph = defaultdict(list)

        for i in edges:

            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        vis = [False] * n

        cnt = 0

        for i in range(n):

            if vis[i] == False:

                ans = bfs(graph , i)

                print(ans)

                if check(ans):

                    cnt += 1

        return cnt





        
