class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        M, P = 10**15 + 7, 31
        prefix_hash_dict = defaultdict(int)

        def idx(char):
            return ord(char) - ord('a') + 1

        def encode_prefixes(s):
            prefix_hash = 0
            p = 1
            for char in s:
                prefix_hash = (prefix_hash + idx(char) * p) % M
                prefix_hash_dict[prefix_hash] += 1
                p = (p * P) % M

        def score(s):
            prefix_hash = res = 0
            p = 1
            for char in s:
                prefix_hash = (prefix_hash + idx(char) * p) % M
                res += prefix_hash_dict[prefix_hash]
                p = (p * P) % M
            return res

        for word in words:
            encode_prefixes(word)

        return [score(word) for word in words]