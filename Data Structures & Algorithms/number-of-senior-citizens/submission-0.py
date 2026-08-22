class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniorcount = 0
        for d in details:
            n = int(d[11]) *10 + int(d[12])
            if n > 60:
                seniorcount +=1
        return seniorcount