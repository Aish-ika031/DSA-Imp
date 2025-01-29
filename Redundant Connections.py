class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        res = [i for i in range(len(edges) + 1)]

        # for i in range(len(edges) +1):

        #     res.append(i)

        def union_find(root):

            if res[root] != root:

                res[root] = union_find(res[root])

            return res[root]

        for i in edges:

            a , b = union_find(i[0]) , union_find(i[1])

            if a == b:

                return [i[0] ,i[1]]

            res[b] = a
