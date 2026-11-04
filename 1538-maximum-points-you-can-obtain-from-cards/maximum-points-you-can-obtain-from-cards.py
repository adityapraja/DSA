class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        left , right = 0, len(cardPoints) - 1
        max = 0
        n = len(cardPoints)        
        if k < 0 or k > n:
            return -1

        for i in range(k):
            max += cardPoints[i]
        
        currentSum = max

        for left in range(k-1,-1,-1):
            currentSum = currentSum - cardPoints[left] + cardPoints[right]
            right -= 1
            if currentSum > max:
                max = currentSum
            
        return max
            


        return max


