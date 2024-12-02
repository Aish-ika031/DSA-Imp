class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentence = sentence.split()

        print(sentence)

        for i in range(0 , len(sentence)):

            print(i)

            cur_word = sentence[i][:len(searchWord)]

            if cur_word == searchWord:

                return i + 1

        return -1
