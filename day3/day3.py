def find_joltages(line, num_digits):
        line = line[:-1]
        nums = [int(n) for n in line]

        digits = ''

        for i in range(num_digits-1, -1, -1):
            dig = max(nums) if i <= 0 else max(nums[:-i])
            index = nums.index(dig)
            nums = nums[index+1:]
            digits += str(dig)
        return int(digits)


with open("day3_input") as file:
    answer = 0
    for line in file:
        answer += find_joltages(line, 12)

    print(answer)