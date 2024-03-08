class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        cnt = Counter(magazine)

        cnt1 = Counter(ransomNote)
        
        for i in ransomNote:

            if i not in magazine or cnt1[i] > cnt[i]: 

                return False
                

        return True