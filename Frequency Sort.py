class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        c = Counter(nums)

        res = []

        # d = sorted(c.values())

        d = sorted(nums, key=lambda kv: (c[kv], -kv))

        return d

        # print(d)

        # for i in d:

        #     print(i)

        #     ky , vl = i[0] , i[1]

        #     while vl != 0:

        #         res.append(ky)

        #         vl -= 1

        # return res

            