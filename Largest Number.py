class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        res = []

        for i in nums:

            # if len(str(i)) == 1:

            #     res.append(str(i))

            # else:

            #     st = 0

            #     while st < len(str(i)):

            #         res.append(str(i)[st])

            #         st += 1

            res.append(str(i))

        # print(res)

        # l1 = list(map(int , res))

        # print(l1)

        res.sort(key = lambda val : val * 10 , reverse = True)

        if res[0] == '0':

            return "0"


        # ans = []

        # for i in l1:

        #     ans.append(str(i))

        return "".join(res)