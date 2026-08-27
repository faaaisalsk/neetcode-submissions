class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)+1):
            cnt = 0
            for n in nums:
                if n>=i:
                    cnt +=1
            
            if cnt == i:
                return i

        return -1