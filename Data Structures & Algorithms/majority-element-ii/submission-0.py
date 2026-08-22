class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums)//3
        res = []
        counter = Counter(nums)
        for n in counter.keys():
            if counter[n] > l:
                res.append(n)
        return res