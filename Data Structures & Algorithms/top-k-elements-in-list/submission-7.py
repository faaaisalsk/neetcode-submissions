class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)
        res = []
        arr = [[]]
        
        for key,v in count.items():
            arr.append([v, key])
        arr.sort()

        while k>0:
            res.append(arr.pop()[1])
            k-=1
        return res
