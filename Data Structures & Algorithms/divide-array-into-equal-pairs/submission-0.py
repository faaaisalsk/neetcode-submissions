class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for n in nums:
            if counter[n]%2 != 0:
                return False
        return True