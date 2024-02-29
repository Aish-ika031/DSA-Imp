class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(val , res , curr):

            if len(curr) == k:

                res.append(curr[:])

                return 

            for i in range(val , n +1):

                curr.append(i)

                backtrack(i+1 , res , curr)

                curr.pop()

                # backtrack(i+1 , res , curr)

        res = []

        backtrack(1 , res , [])

        return res
        