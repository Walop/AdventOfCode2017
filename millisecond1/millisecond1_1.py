with open("input", "r") as file:
    input = file.read()
    nums = list(input)
    sum = 0
    for i in range(0, len(nums)):
        if nums[i] == nums[i-1]:
            sum += int(nums[i])
    print(sum)
