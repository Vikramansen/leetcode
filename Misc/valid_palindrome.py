def isAnagram(s,t):
    dict_s = {}
    dict_t = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        dict_s[s[i]]= 1 + dict_s.get(s[i], 0)
        dict_t[t[i]] = 1 + dict_t.get(t[i], 0)
    return dict_s == dict_t

def main():
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s,t))

main()