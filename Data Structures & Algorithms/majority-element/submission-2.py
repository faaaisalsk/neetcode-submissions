class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n= len(nums)
        hashmap = {}
        for c in nums:
            if hashmap.get(c,0) == n//2:
                return c
            hashmap[c] = 1 + hashmap.get(c,0)