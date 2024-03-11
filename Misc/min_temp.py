class Solution:
    def dailyTemperatures(self, temp):
        stack = []
        res = [0] * len(temp)
        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                last = stack.pop()
                res[last] = i - last
            stack.append(i)
        return res

def main():
    a = [1,2,1,2,3,4,5]
    print(Solution().dailyTemperatures(a))

main()

