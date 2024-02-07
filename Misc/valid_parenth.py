class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")":"(","}":"{","]":"["}
        for p in s:
            if p in dict:
                if stack and stack[-1] == dict[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False   
def main():
    s ="[(({{(})}}))]"
    print(Solution().isValid(s))
main()