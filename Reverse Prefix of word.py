class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        idx = 0

        for i in range(len(word)):

            if word[i] == ch:

                idx = i

                break

        rev_str = word[0 : idx + 1][::-1]

        return rev_str + word[idx + 1 : ]