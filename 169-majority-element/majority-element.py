class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = dict()
        for i in range(0,len(nums)):
            if nums[i] in count:
                count[nums[i]]+=1
            else:
                count[nums[i]]=1

        for i in count:
            if count[i] > len(nums)/2:
                return i


        
