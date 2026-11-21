class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        power = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                power+=1
                ans = max(ans,power)
            else:
                power = 1
            
        
        return ans