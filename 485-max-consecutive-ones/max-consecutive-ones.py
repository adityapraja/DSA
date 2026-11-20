class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxarr = 0
        current = 0
        for n in nums:

            if n == 0:
                # maxarr = max(maxarr,current)
                current = 0
            else:
                current+=1
                maxarr = max(maxarr,current)
            

        return maxarr

