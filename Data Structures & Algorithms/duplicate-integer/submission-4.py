class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnums = set()
        for n in nums:
            if n in setnums:
                return True
            setnums.add(n)
        return False
