class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        l = int(len(nums)/2)

        for n in nums:
            counter[n] = 1 + counter.get(n,0)
            if counter[n] > l:
                return n