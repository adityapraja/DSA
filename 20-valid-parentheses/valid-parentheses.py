class Solution:
    def isValid(self, s: str) -> bool:
        char = list()
        i = 0
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                char.append(s[i])
            else:
                if not char:
                    return False
                top = char.pop()
                if s[i] ==')' and top!= '(':
                    return False
                if s[i] =='}' and top!= '{':
                    return False
                if s[i] ==']' and top!= '[':
                    return False

        return len(char) == 0