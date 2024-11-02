class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        sentence = sentence.split(" ")

        print(sentence)
        
        prev = sentence[0]

        print(prev)

        cnt = 0

        for i in range(1 , len(sentence)):

            # print(0)

            # print(sentence[i][0])

            # print(prev[-1])

            if sentence[i][0] == prev[-1]:

                print(0)

                prev = sentence[i]

                cnt += 1

            else:

                return False

        # print(cnt)

        return True if sentence[0][0] == sentence[-1][-1] and cnt + 1 == len(sentence) else False
