class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        numset1 = set(nums1)
        numset2 = set(nums2)
        res1, res2 = [], []
        for n in numset1:
            if n not in numset2:
                res1.append(n)
        for n in numset2:
            if n not in numset1:
                res2.append(n)
        return [res1, res2] 