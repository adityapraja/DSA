class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        dup = set()

        for i in range(0,len(nums)):
            if i > k:
                dup.remove(nums[i-k-1])
            
            if nums[i] in dup:
                return True
            
            dup.add(nums[i])

            
        return False
