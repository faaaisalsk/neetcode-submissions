class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = sumf = nums[0]
        for i in range(1, len(nums)):
            if nums[i]> nums[i-1]:
                sumf += nums[i]
            else: 
                sumf = 0
                sumf += nums[i]
            maxSum = max(maxSum, sumf)
        return maxSum