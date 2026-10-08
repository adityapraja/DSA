class Solution:
    def isPalindrome(self, s: str) -> bool:
        # an = {' ',':',';',',','.','/','?','@','!','#','$','%','^','&','*','-','_','`','~','(',')','{','}',']','[','|','"','\\'}
        s = s.lower()
        chars = [c for c in s if c.isalnum()]
        s = ''.join(chars)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1

        return True
