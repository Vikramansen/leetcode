class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        n = len(height)
        r = n - 1
        left_max, right_max = height[0], height[r]
        res = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        return res
    
def main():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))
main()