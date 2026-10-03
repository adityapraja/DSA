class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numbers = set()
        dup = False
        for x in range(len(nums)):
            if nums[x] in numbers:
                return True
            else:
                numbers.add(nums[x]) 

        return False