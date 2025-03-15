class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def check(nums,k,mid):

            i = 0

            while i < len(nums):

                if nums[i] <= mid:

                    k -= 1

                    i += 2

                else:

                    i += 1

                if k == 0:

                    return True

            return False

        
        low , high , ans = 1 , int(1e9+1) , int(1e9+1)

        while low<high:

            mid = low + (high-low)//2

            if check(nums, k , mid):

                ans = min(ans , mid)

                high= mid

            else:

                low = mid + 1

        return ans
