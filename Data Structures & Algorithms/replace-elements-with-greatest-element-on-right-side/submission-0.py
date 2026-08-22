class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rMax = -1
        for i in range(len(arr)-1,-1,-1):
            pMax = arr[i]
            arr[i] = rMax
            rMax = max(pMax, rMax)
        return arr