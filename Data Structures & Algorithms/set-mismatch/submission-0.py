class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        duplicate = missing = 0

        for i in range(1, len(nums) + 1):
            if count[i] == 0:
                missing = i
            if count[i] ==2:
                duplicate = i

        return [duplicate, missing]
