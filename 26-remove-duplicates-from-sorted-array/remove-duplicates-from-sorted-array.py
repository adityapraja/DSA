class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        right = 1
        k = 1
        while right < len(nums):
           
            if nums[left] != nums[right]:
                nums[left+1] = nums[right]
                left+=1
                k+=1

            right +=1

        return k


                 