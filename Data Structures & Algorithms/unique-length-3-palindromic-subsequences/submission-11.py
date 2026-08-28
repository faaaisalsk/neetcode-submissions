class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0

        for ch in set(s):
            left = s.find(ch)
            right = s.rfind(ch)

            if right - left > 1:
                res += len(set(s[left + 1:right]))

        return res