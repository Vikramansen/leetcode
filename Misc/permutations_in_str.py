class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0, 0
        lens1, lens2 = len(s1), len(s2)
        dicts1 = {}
        dictwin = {}
        for char in s1:
            dicts1[char] = 1 + dicts1.get(char,0)
        while r < len(s2):
            dictwin[s2[r]] = 1 + dictwin.get(s2[r],0)
            if (r-l+1) > len(s1):
                dictwin[s2[l]] -= 1
                if dictwin[s2[l]] == 0:
                    del dictwin[s2[l]]
                l +=1
            if dictwin == dicts1:
                return True
            r+=1
        return False

def main():
    s1 = "aab"
    s2 = "awsdasxb"
    print(Solution().checkInclusion(s1,s2))
main()