class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        cnt = [0] * 3

        for i in s:

            cnt[ord(i) - ord('a')] += 1

        st ,end = 0 , 0

        if cnt[0] < k or cnt[1] < k or cnt[2] < k:

                return -1

        for end in range(len(s)):

            cnt[ord(s[end]) - ord('a')] -= 1

            if cnt[0] < k or cnt[1] < k or cnt[2] < k:

                cnt[ord(s[st]) - ord('a')] += 1

                st += 1

        val = len(s) - end + st

        return val - 1
            

            
        
