class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        arr = [0]*len(nums)
        p = 0
        n = 1
        for i in range(0,len(nums)): 
            if nums[i] > 0:
                arr[p] = nums[i]
                p+=2
            else:
                arr[n] = nums[i] 
                n+=2

        return arr