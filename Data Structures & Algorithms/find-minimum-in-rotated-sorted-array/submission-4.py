class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                res = min(res, nums[i])
        return res