from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count_t = Counter(t)
        window = {}
        res, res_len = [-1,-1], float("infinity")
        have, need = 0, len(count_t)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in count_t and count_t[c] == window[c]:
                have += 1
            while have == need:
                if (r-l+1) < res_len:
                    res = [l,r]
                    res_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l:r+1] if res_len != float("infinity") else ""

def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s,t))
main()