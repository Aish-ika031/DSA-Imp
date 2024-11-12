class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        res = [0] * len(queries)

        items.sort(key = lambda a : a[0])

        l1 = []

        for i in range(len(queries)):

            l1.append([queries[i] , i])

        l1.sort(key = lambda a : a[0])

        idx ,mx = 0 , 0

        for i in range(len(queries)):

            a , b  = l1[i][0] , l1[i][1]

            while idx < len(items) and items[idx][0] <= a:

                mx = max(mx , items[idx][1])

                idx += 1

            res[b] = mx

        return res
