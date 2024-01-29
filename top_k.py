def topKFrequent(nums,k):
    dic = {}
    freq = [[] for _ in range(len(nums) + 1)] 
    res = []

    for num in nums:
        dic[num] = 1 + dic.get(num, 0)

    for key, value in dic.items():
        freq[value].append(key)

    for i in range(len(freq)-1,0,-1):
        for num in freq[i]:
            if len(res) < k:
                res.append(num)

    return res

def main():
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums,k))
    
main()