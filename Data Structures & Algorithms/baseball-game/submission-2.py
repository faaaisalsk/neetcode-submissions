class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stackops = []
        
        for o in operations:
            if o == "+":
                stackops.append(stackops[-1]+ stackops[-2])
            elif o == "D":
                stackops.append(2 * stackops[-1])
            elif o == "C":
                stackops.pop()
            else:
                stackops.append(int(o))
        return sum(stackops)
