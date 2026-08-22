class Solution:
    def findLucky(self, arr: List[int]) -> int:
        countarr = Counter(arr)
        res = -1
        for n in countarr:
            if countarr[n] == n:
                res = max(n, res)
        return res