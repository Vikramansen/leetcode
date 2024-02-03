def groupAnagrams(strs):
    dic = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in dic:
            dic[sorted_word] = []
        dic[sorted_word].append(word)
    return dic.values()

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))

main()
