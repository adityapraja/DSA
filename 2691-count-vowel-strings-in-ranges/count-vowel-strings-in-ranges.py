class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        prefix = [0] * (len(words)+1)
        i = 0
        ans =[]
        for word in words:
            if (word[0] in ' aieou' and word[-1] in ' aieou' ) or word.lower() in 'aieou':
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]
            i+=1

        for query in queries:
            l = query[0]
            r = query[1]
            ans.append(prefix[r] - prefix[l-1])


        return ans