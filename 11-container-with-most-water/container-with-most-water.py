class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater = - float('inf')
        
        if len(height) < 2:
            return 0
        
        left, right = 0, len(height) - 1

        while left <= right:
            currentWidth = right - left 
            currentHeight = min(height[right],height[left])
            currentWater = currentWidth * currentHeight
            maxWater = max(maxWater,currentWater)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return maxWater