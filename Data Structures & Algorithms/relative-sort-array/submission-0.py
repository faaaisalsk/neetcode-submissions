class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        countarr1 = Counter(arr1)
        arr2set = set(arr2)
        arr3=[]
        arr4 = []
        for a in arr2:
            if a in countarr1:
                while countarr1[a]>0:
                    arr3.append(a)
                    countarr1[a] -=1
        
        for a in arr1:
            if a not in arr2set:
                arr4.append(a)
        arr4.sort()

        return arr3 + arr4