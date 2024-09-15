class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        vowels = ['a' , 'e' , 'i' , 'o' , 'u']

        v1 = {'a' : 1 , 'e' : 2 , 'i': 4, 'o' : 8 , 'u' :16}

        mx = 0

        xor = 0

        d1 = {0: -1}

        for i in range(len(s)):

            if s[i] in vowels:

                xor = xor ^ v1[s[i]]

            if xor in d1:

                mx = max(mx , i - d1[xor])

            else:

                d1[xor] = i

        return mx