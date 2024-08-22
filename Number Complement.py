class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a=""

        s1=bin(num)

        s1=s1[2:]

        for i in s1:

            if i=="1":

                a=a+"0"

            elif i=="0":

                a=a+"1"
                
        return int(a,2)