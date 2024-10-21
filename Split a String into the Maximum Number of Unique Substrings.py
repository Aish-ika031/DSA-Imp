class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def recur(s , idx , s1 , mx):

            if idx == len(s):

                mx[0] = max(mx[0] , len(s1))

                return 

            substring = ""

            for i in range(idx , len(s)):

                substring += s[i]

                if substring not in s1:

                    s1.add(substring)

                    recur(s , i + 1 , s1 , mx)

                    s1.remove(substring)

            print(mx)

            # return mx

        mx = [0]

        s1 = set()

        recur(s , 0 , s1 , mx)

        return mx[0]
