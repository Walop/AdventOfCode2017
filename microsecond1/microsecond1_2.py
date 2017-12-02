with open("input", "r") as file:
    input = file.read()
    nums = list(input)
    sum = 0
    skip = int(len(nums)/2)
    for i in range(0, len(nums)):
        j = i + skip
        j = j if j < len(nums) else j - len(nums)
        if nums[i] == nums[j]:
            sum += int(nums[i])
    print(sum)
