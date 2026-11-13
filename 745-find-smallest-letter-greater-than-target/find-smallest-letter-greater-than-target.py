class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        low , high = 0, len(letters) - 1
        
        smallestChar = letters[0]
        while low <= high:
            mid = (low + high) // 2

            if ord(letters[mid]) > ord(target):
                high = mid - 1
                smallestChar = letters[mid]
            else:
                low = mid + 1
            
        return smallestChar