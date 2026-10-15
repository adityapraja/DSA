class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        str1 = 0
        str2 = len(needle)

        while str2 <= len(haystack):
            if haystack[str1:str2] == needle:
                return str1

            str1+=1
            str2+=1

        
        return -1