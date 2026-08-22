class Solution:
    def minOperations(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            if i %2 == 0:
                cnt +=1 if s[i] == '0' else 0
            else:
                cnt +=1 if s[i] == '1' else 0
        return min(cnt, len(s) -  cnt)