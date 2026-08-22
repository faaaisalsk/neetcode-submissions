class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = descreasing = 1
        longest = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                increasing = descreasing = 1
            elif nums[i] > nums[i-1]:
                increasing +=1
                descreasing = 1
            else:
                descreasing +=1
                increasing = 1

            longest = max(longest, increasing, descreasing)
        return longest
