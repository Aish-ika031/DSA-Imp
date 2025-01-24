class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def check_cycle_using_dfs(node,path_vis,graph,vis,check):

            vis[node]=1
            path_vis[node]=1

            for adj_neigh in graph[node]:

                if vis[adj_neigh]!=1:

                    if check_cycle_using_dfs(adj_neigh,path_vis,graph,vis,check)==True:

                        return True

                elif path_vis[adj_neigh]:

                    return True

            check[node]=1
            path_vis[node]=0

            return False

        vis=[0]*len(graph)
        path_vis=[0]*len(graph)
        check=[0]*len(graph)

        safe_nodes=[]

        for i in range(0,len(graph)):

            if vis[i]!=1:
                check_cycle_using_dfs(i,path_vis,graph,vis,check)

        for i in range(len(graph)):

            if check[i]==1:

                safe_nodes.append(i)

        return safe_nodes


        
