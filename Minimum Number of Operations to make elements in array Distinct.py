class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        s1 = set()

        idx = -1

        for i in range(len(nums)-1 , -1 , -1):

            if nums[i] not in s1:

                s1.add(nums[i])

            else:

                idx = i

                break

        val = idx + 3

        return val //3

            
