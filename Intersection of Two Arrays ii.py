class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        cnt1 , cnt2 = Counter(nums1) , Counter(nums2)

        res = []

        for i in nums2:

            if cnt1[i] > 0 :

                res.append(i)

                cnt1[i] -= 1

        return res        