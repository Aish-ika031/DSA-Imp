class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        mn = min(nums)

        if k > mn:

            return -1

        s1= set()

        for i in nums:

            if i > k:

                s1.add(i)

        return len(s1)
