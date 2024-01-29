def longestConsecutive(nums):
    numset = set(nums)
    longest = 0
    for num in nums:
        if (num - 1) not in numset:
            length  = 0
            while (num + length) in numset:
                length += 1
            longest = max(longest, length)
    return longest

def main():
    nums = [100, 4, 200, 1, 3, 2, 5, 6]
    print(longestConsecutive(nums))
    
main()