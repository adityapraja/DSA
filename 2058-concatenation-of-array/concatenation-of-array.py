from array import *
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(0,2*len(nums)):
            if i < len(nums):
                ans.append(nums[i])
            else:
                ans.append(nums[i - len(nums)])
        
        return ans
