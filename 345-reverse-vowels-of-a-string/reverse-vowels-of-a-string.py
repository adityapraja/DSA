class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = {'a','i','e','u','o','A','I','E','U','O'}
        left = 0
        right = len(s)-1

        while left < right:
            if chars[left] in vowels and chars[right] in vowels:
                temp = chars[left]
                chars[left] = chars[right]
                chars[right] = temp
                left+=1
                right-=1

            elif chars[left] not in vowels:
                left+=1
            elif chars[right] not in vowels:
                right-=1

            

        strs = "".join(chars)
        return strs
