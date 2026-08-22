class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        l = int(len(nums)/2)

        for n in nums:
            if hashmap[n] > l:
                return n