class Solution:
    def maximumLength(self, s: str) -> int:
        
        mp = defaultdict(int)

        for i in range(len(s)):

            for j in range(len(s)):

                cur = ''

                for k in range(i,j + 1):

                    cur += s[k]

                mp[cur] += 1

        res = ''

        for i in range(len(s)):

            for j in range(len(s)):

                cur = ''

                for k in range(i,j + 1):

                    cur += s[k]

                s1 = set(cur)

                if len(s1) ==1 and mp[cur] > 2:

                    if len(cur) > len(res):

                        res = cur

        return len(res) if len(res) > 0 else -1
