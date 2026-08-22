class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = []
        hashset = set(nums)
        n = len(nums)
        for num in range(1, n+1):
            if num not in hashset:
                arr.append(num)
        return arr