class Solution:

    def palindrome(self,s: str,l: int,r: int)-> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            
            l+=1
            r-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return self.palindrome(s,left+1,right) or self.palindrome(s,left,right-1)

        return True
        
      
    