class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        kbeauty = 0
        number = str(num)
        left,right  = 0, k-1

        while right < len(number):
            sub = int(number[left:right+1])
            if sub != 0 and num % sub == 0:
                kbeauty+=1
            left+=1
            right+=1
        
        return kbeauty
