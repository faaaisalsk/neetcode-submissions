class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        arr = []
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        return res