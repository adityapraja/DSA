class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        v = sorted(strs)

        first = v[0]
        last = v[len(v)-1]

        for i in range(len(min(first,last))):
            if first[i] != last[i]:
                return prefix
            else:
                prefix+=first[i]
        return prefix