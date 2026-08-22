class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct, seen = set(), set()
        res = ""

        for a in arr:
            if a in distinct:
                distinct.remove(a)
                seen.add(a)

            elif a not in seen:
                distinct.add(a)
        
        for s in arr:
            if s in distinct:
                k -=1
                if k == 0:
                    return s

        return ""
