class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnums = set(nums)
        return False if len(setnums) == len(nums) else True
