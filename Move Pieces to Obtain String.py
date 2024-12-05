class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        s , t = [] , []

        for i in range(len(start)):

            if start[i] != '_':

                s.append((start[i],i))

        for i in range(len(start)):

            if target[i] != '_':

                t.append((target[i], i))

        if len(s) != len(t):

            return False

        while len(s) > 0:

            s1 , t1 = s.pop(0) , t.pop(0)

            if (s1[0] != t1[0] or (s1[0] =='L' and s1[1] < t1[1]) or (s1[0] == 'R' and s1[1] > t1[1])):

                return False

        return True

            
