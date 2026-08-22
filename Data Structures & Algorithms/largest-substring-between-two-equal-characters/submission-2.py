class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_ind = {}
        res = -1

        for i, c in enumerate(s):
            if c in char_ind:
                res = max(res, i - char_ind[c]-1)

            else:
                char_ind[c] = i
        return res