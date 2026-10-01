from array import *
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = [0] * (2 * len(nums))
        for i in range(0,len(ans)):
            ans[i] = nums[i % len(nums)]
        return ans
