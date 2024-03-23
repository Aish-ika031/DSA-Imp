class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        res = ''

        for i in s:

            res += i if i.isalnum() else ''

        print(res , res[::-1])

        return True if res == res[::-1] else False

        