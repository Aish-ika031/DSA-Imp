class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        s1 , s2 = sentence1.split() , sentence2.split()

        s1 , s2 = deque(s1) , deque(s2)

        while s1 and s2:

            if s1[0] == s2[0]:

                s1.popleft()

                s2.popleft()

            else:

                break

        print(len(s1) , len(s2))

        while s1 and s2:

            if s1[-1] == s2[-1]:

                s1.pop()

                s2.pop()

            else:

                break

        print(len(s1) , len(s2))

        return True if len(s1) == 0  or len(s2) == 0 else False