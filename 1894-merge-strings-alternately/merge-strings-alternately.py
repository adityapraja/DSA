class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedword = ""

        one = 0
        two = 0
        i = 0
        maxm = max(len(word1),len(word2))
        while i < maxm:
            if one < len(word1):
                mergedword += word1[one]
                one+=1
            if two < len(word2):
                mergedword += word2[two]
                two+=1
            i+=1

        return mergedword