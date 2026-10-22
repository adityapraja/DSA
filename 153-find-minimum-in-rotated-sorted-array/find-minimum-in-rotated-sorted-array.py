class Solution:
    def findMin(self, nums: list[int]) -> int:
        min = nums[0]

        for i in range(0,len(nums)):
            if nums[i] < min:
                return nums[i]
            
            
        return min
    
