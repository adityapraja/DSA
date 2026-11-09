class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top ,bot = 0, rows - 1

        while top <= bot:
            mid = (top + bot) // 2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        row = (top+bot) // 2
        l,r = 0, cols-1

        while l <= r:
            mid = (l+r) // 2

            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
            
        return False

            