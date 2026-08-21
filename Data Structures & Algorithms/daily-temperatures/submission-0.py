class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [len(temperatures) - 1]
        for i in range(len(temperatures) - 2, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res