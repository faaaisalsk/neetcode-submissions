class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        count = {}
        res = []
        for n, h in zip(names, heights):
            count[h] = n
        
        heights = sorted(heights, reverse = True)

        for h in heights:
            res.append(count[h])
        
        return res