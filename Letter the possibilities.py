class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def backtrack(counter):
            count = 0
            for ch in counter:
                if counter[ch] > 0:
                    counter[ch] -= 1
                    count += 1 + backtrack(counter)
                    counter[ch] += 1
            return count
            
        return backtrack(Counter(tiles))
