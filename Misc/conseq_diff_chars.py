class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        check = set()
        res = 0
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l+=1
            check.add(s[r])
            res = max(res, r-l+1)
        return res
    
def main():
    s = "abcdeaswd"
    print(Solution().lengthOfLongestSubstring(s))

main()