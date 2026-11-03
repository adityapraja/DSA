class Solution:
    def firstOcc(self, nums,target):
        left , right = 0, len(nums) - 1
        ans = -1
        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid -1

            elif nums[mid] < target:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        
        return ans


    def lastOcc(self,nums,target):
        left , right = 0, len(nums) - 1
        ans = -1
        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid -1

            elif nums[mid] < target:
                left = mid + 1
            else:
                ans = mid
                left = mid + 1
        return ans


    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = self.firstOcc(nums,target)

        if first == -1:
            return [-1,-1]
        
        return [first,self.lastOcc(nums,target)]
