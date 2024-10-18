class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        def recur(i , nums , n , res , cur):

            if i >= n:

                val = 0

                for i in res:

                    val = val | i

                curr.append(val)

                return 

            res.append(nums[i])

            recur(i + 1 , nums , n , res , curr)

            res.pop()

            recur(i + 1 , nums , n , res , curr)

            return 

        
        res , curr = [] , []

        recur(0 , nums , len(nums) , res , curr)

        c = Counter(curr)

        ans = []

        for i in c.values():

            ans.append(i)

        return max(ans)
