class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        output = [0] * len(temperatures)
        stack = []

        # Monotonically decreasing stack which keeps track of indexes
        for i in range(len(temperatures)):
            while (stack and temperatures[i] > temperatures[stack[-1]]):
                j = stack.pop()
                output[j] = i - j
            stack.append(i)
        
        return output