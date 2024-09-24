class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        s1 = set()

        for i in arr1:

            while i not in s1 and i > 0:

                s1.add(i)

                i = i // 10

        cnt = 0

        for i in arr2:

            while i not in s1 and i > 0:

                i = i // 10

            if i > 0:

                cnt = max(cnt , len(str(i)))

        return cnt