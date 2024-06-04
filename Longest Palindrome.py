from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        mid=0

        l1=Counter(s)

        for i in l1:

            mid=mid+l1[i]//2*2

            if mid%2==0 and l1[i]%2==1:

                mid=mid+1
                
        return mid
        