class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:

        j = 0
        
        for i in range(len(s)):

            if s[i] == s[j]:

                continue

            if i-j ==k :

                return True

            j = i

        val = len(s) - i

        return True if val == k else False
