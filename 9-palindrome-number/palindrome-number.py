class Solution:
    def isPalindrome(self, x: int) -> bool:
        revNum = 0
        num = x

        while num > 0:
            digit = num % 10
            revNum = (revNum * 10 ) + digit
            num = num // 10
        

        return revNum == x