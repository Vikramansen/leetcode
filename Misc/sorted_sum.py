def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l <= r:
        find = numbers[l] + numbers[r]
        if find == target:
            return [l+1,r+1]
        if find < target:
            l+=1
        else:
            r-=1
def main():
    numbers = [2,7,11,15]
    target = 9
    print(twoSum(numbers,target))