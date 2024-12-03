class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        
        res = []

        st , end = 0 , 0

        while end <len(spaces):

            if st == spaces[end]:

                res.append(' ')

                end += 1
            
            res.append(s[st])

            st += 1

        while st < len(s):

            res.append(s[st])

            st += 1

        return "".join(res)
