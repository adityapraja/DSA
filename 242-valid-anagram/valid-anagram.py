class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charCount = dict()

        for x in s:
            if x not in charCount:
                charCount[x] = 1
            else:
                charCount[x]+=1
        
        for x in t:
            if x not in charCount or charCount[x] == 0:
                return False
            else:
                charCount[x]-=1

        return True