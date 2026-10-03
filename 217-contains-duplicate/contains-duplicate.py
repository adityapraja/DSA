class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dup = False
        nums.sort()
        for x in range(len(nums)):
            if x <= (len(nums)- 2) and nums[x] == nums[x+1]:
                dup = True

        
        return dup