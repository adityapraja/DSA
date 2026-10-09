class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left = 0
        right = k-1
        maxavg = 0
        sum = 0
        for i in range(0,k):
            sum+=nums[i]

        avg = sum / k
        maxavg = avg

        while right < len(nums) - 1:
            sum -= nums[left]
            left+=1
            right+=1
            sum += nums[right]

            avg = sum/k

            if avg > maxavg:
                maxavg = avg

        
        return maxavg
        