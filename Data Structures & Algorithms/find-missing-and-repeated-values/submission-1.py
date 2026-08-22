class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hasht = {}
        N = len(grid)
        for i in range(N):
            for j in range(N):
                if grid[i][j] not in hasht:
                    hasht[grid[i][j]] = 0
                hasht[grid[i][j]] +=1
        
        double, missing = 0,0
        for num in range(1, N*N + 1):
            if num not in hasht:
                missing = num
            elif hasht[num] == 2:
                double = num
        return [double, missing]

