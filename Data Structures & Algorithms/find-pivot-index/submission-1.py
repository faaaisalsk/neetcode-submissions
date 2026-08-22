class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0

        for i in range(len(nums)):
            if leftsum * 2 == total - nums[i]:
                return i
            leftsum += nums[i]

        return -1