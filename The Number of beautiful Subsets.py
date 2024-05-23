class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def generate_subset(nums , k):

            res = [[]]

            for i in nums:

                dummy = res[::]

                for j in dummy:

                    if i - k not in j:

                        res.append(j+[i])

            return res

        nums.sort()

        res = (generate_subset(nums , k)) 

        # print(res)

        return len(res) - 1


            