class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = Counter(text)
        balloon = Counter("balloon")
        res = len(text)

        for t in balloon:
            res = min(res, hashmap[t] // balloon[t])
        return res