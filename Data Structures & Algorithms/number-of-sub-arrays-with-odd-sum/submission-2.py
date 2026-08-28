class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        curr_sum = 0
        odd_cnt = 0
        even_cnt = 0
        res = 0
        mod = 10**9 + 7

        for n in arr:
            curr_sum +=n

            if curr_sum %2:
                res = (res+1 + even_cnt) % mod
                odd_cnt +=1
            else:
                res = (res + odd_cnt) % mod
                even_cnt +=1
        return res