class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        def func(word , d1):

            for i in range(len(word)):

                root = word[0 : i]

                if root in d1:

                    return root

            return word
        
        sen = sentence.split()

        d1 = set(dictionary)

        for i in range(len(sen)):

            sen[i] = func(sen[i] , d1)

        return " ".join(sen)

