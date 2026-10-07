class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = []
        mp = dict()
        word = ""
        ans = []
        for i in range(0,len(strs)):
            word = ''.join(sorted(strs[i]))

            if word not in mp:
                mp[word] = []

            mp[word].append(strs[i])

        
        for x in mp:
            ans.append(mp[x])

        return ans
