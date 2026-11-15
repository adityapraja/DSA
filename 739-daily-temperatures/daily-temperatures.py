class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        futureDays = []
        for i in range(n-1,-1,-1):
            while futureDays and temperatures[i] >= temperatures[futureDays[-1]]:
                futureDays.pop()
            if futureDays:
                ans[i] = futureDays[-1] - i
                
            futureDays.append(i)

        return ans