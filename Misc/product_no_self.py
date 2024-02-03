def productExceptSelf(nums):
    res = [1] * len(nums)
    prefix, postfix = 1, 1
    for i in range(len(nums)):
        res[i] =  prefix 
        prefix *= nums[i]
    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

def main():
    nums = [1,2,3,4]
    print(productExceptSelf(nums))

main()