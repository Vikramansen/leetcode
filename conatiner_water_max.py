class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0
        while l < r:
            max_water = max(max_water, min(height[l], height[r]) * (r-l))
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return max_water
def main():
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))
main()