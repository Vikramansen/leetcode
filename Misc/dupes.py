def findDuplicates(nums):
    nums_dict = {}
    res = []
    for num in nums:
        nums_dict[num] = 1 + nums_dict.get(num, 0)
    for key, value in nums_dict.items():
        if value > 1:
            res.append(key)
    return res
def main():
    nums = [4,3,2,7,8,2,3,1]
    print(findDuplicates(nums))
main()